def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 50:
        return substrings
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50 and substring not in substrings:
            substrings.append(substring)
    return substrings