def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 99:
        return substrings
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(set(substring)) == 99:
            substrings.append(substring)
    return list(set(substrings))