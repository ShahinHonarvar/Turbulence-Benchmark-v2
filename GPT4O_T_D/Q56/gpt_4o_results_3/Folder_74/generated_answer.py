def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    for i in range(length - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97:
            substrings.append(substring)
    return list(set(substrings))