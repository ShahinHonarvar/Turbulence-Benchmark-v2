def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 30:
        return substrings
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            substrings.append(substring)
    return substrings