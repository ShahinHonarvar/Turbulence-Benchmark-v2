def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 7):
        substring = s[i:i + 85]
        if len(set(substring)) == 85:
            substrings.append(substring)
    return substrings