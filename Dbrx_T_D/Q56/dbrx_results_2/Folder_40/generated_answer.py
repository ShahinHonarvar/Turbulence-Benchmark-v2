def all_substring_of_size_n(s: str) -> list:
    substrings = []
    if len(s) < 2:
        return substrings
    for i in range(len(s) - 1):
        substring = s[i:i + 2]
        if len(substring) == 2:
            if substring[0] != substring[1]:
                substrings.append(substring)
    return list(set(substrings))