def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 32 + 1):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            substrings.append(substring)
    return list(set(substrings))