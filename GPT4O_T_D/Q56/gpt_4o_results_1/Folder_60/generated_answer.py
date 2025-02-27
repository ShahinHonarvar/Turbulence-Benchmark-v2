def all_substring_of_size_n(s):
    if len(s) < 36:
        return []
    substrings = set()
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)