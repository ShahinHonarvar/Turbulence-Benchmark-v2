def all_substring_of_size_n(s: str) -> list:
    substrings = []
    seen_substrings = set()
    n = 16
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen_substrings:
            substrings.append(substring)
            seen_substrings.add(substring)
    return substrings