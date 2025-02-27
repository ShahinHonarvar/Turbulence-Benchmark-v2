def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 16:
        return substrings
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16 and substring not in substrings:
            substrings.append(substring)
    return substrings