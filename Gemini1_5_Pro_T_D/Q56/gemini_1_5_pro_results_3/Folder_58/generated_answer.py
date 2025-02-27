def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 127 + 1):
        substring = s[i:i + 127]
        if len(set(substring)) == 127 and substring not in substrings:
            substrings.append(substring)
    return substrings