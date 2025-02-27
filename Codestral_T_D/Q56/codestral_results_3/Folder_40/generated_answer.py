def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 1):
        substring = s[i:i + 2]
        if len(set(substring)) == 2:
            substrings.append(substring)
    return substrings