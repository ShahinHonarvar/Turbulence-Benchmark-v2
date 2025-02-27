def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 96:
        return substrings
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if len(set(substring)) == 96:
            substrings.append(substring)
    return set(substrings)