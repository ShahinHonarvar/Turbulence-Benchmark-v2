def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if len(set(substring)) == 7:
            substrings.add(substring)
    return list(substrings)