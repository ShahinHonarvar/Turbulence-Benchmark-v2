def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 1):
        substring = s[i:i + 2]
        if len(set(substring)) == 2:
            substrings.add(substring)
    return list(substrings)