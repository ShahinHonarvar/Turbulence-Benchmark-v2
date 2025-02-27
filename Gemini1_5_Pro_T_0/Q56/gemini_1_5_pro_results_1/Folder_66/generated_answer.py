def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if len(set(substring)) == 26 and substring not in substrings:
            substrings.append(substring)
    return substrings