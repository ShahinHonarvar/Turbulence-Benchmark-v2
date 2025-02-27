def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            substrings.append(substring)
    return substrings