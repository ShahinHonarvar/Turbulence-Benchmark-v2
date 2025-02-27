def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 81:
        return substrings
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if len(set(substring)) == 81:
            if substring not in substrings:
                substrings.append(substring)
    return substrings