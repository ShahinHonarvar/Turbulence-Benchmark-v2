def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 37:
        return substrings
    for i in range(len(s) - 36):
        substring = s[i:i + 37]
        if len(set(substring)) == 37:
            if substring not in substrings:
                substrings.append(substring)
    return substrings