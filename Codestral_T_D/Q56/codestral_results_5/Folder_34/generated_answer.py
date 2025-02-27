def all_substring_of_size_n(s):
    if len(s) < 84:
        return []
    substrings = set()
    for i in range(len(s) - 84 + 1):
        substring = s[i:i + 84]
        if len(set(substring)) == 84:
            substrings.add(substring)
    return list(substrings)