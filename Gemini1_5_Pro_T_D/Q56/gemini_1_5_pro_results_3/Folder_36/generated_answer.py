def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 146:
        return substrings
    for i in range(len(s) - 145):
        substring = s[i:i + 146]
        if len(set(substring)) == 146 and substring not in substrings:
            substrings.append(substring)
    return substrings