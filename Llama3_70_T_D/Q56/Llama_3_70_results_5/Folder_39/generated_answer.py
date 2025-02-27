def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 94 + 1):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            substrings.add(substring)
    return list(substrings)