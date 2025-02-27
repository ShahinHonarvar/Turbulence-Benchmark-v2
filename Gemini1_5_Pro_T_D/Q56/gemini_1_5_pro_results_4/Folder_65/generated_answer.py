def all_substring_of_size_n(s: str) -> list:
    substrings = []
    if len(s) < 81:
        return substrings
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if len(set(substring)) == 81:
            substrings.append(substring)
    return substrings