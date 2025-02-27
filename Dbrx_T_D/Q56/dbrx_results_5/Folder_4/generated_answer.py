def all_substring_of_size_n(s: str) -> List[str]:
    result = []
    for i in range(len(s) - 41 + 1):
        substring = s[i:i + 41]
        if len(set(substring)) == 41:
            result.append(substring)
    return result