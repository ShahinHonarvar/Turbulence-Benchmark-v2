def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if len(substring) == 10 and len(set(substring)) == 10:
            substrings.add(substring)
    return list(substrings)