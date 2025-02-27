def all_substring_of_size_n(s: str) -> list[str]:
    if len(s) < 106:
        return []
    substrings = []
    for i in range(len(s) - 105):
        substring = s[i:i + 106]
        if len(set(substring)) == 106 and substring not in substrings:
            substrings.append(substring)
    return substrings