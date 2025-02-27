def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 100 + 1):
        substring = s[i:i + 100]
        if len(set(substring)) == 100:
            substrings.add(substring)
    return list(substrings)