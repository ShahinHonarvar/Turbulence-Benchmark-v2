def all_substring_of_size_n(s: str) -> List[str]:
    n = 100
    substrings = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))