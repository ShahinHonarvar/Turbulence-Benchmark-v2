def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 66):
        substring = s[i:i + 67]
        if len(set(substring)) == 67:
            substrings.append(substring)
    return list(set(substrings))