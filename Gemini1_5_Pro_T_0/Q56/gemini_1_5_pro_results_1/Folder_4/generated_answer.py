def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if len(set(substring)) == 41 and substring not in substrings:
            substrings.append(substring)
    return substrings