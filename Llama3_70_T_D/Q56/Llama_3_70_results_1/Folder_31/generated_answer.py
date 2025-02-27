def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 46 + 1):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            substrings.add(substring)
    return list(substrings)