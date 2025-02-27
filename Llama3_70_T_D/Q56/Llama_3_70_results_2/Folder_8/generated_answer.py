def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            substrings.add(substring)
    return list(substrings)