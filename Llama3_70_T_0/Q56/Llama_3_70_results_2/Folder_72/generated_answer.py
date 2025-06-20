def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 87):
        substring = s[i:i + 88]
        if len(set(substring)) == 88:
            substrings.add(substring)
    return list(substrings)