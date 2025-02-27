def all_substring_of_size_n(s: str) -> list:
    substrings = []
    if len(s) < 143:
        return substrings
    for i in range(len(s) - 143 + 1):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            if substring not in substrings:
                substrings.append(substring)
    return substrings