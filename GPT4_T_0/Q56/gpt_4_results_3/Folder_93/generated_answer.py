def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(set(s[i:i + 54])) == 54:
            substrings.add(s[i:i + 54])
    return list(substrings)