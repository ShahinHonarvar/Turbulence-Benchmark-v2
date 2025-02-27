def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if len(substring) == 57 and len(set(substring)) == 57:
            substrings.add(substring)
    return list(substrings)