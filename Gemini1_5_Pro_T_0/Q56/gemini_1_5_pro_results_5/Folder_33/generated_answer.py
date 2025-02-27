def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 105 + 1):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            substrings.append(substring)
    return substrings