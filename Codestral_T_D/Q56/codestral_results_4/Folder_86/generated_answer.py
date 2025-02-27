def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            substrings.append(substring)
    return substrings