def all_substring_of_size_n(s: str) -> list:
    substrings = []
    if len(s) < 63:
        return substrings
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(set(substring)) == 63:
            if substring not in substrings:
                substrings.append(substring)
    return substrings