def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 60 + 1):
        substring = s[i:i + 60]
        if len(set(substring)) == 60:
            substrings.add(substring)
    return list(substrings)