def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 74):
        subset = s[i:i + 75]
        if len(set(subset)) == 75:
            substrings.append(subset)
    return substrings