def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 89 + 1):
        substring = s[i:i + 89]
        if len(set(substring)) == 89:
            substrings.add(substring)
    return list(substrings)