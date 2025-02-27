def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 97:
        return substrings
    for i in range(len(s) - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97:
            if substring not in substrings:
                substrings.append(substring)
    return substrings