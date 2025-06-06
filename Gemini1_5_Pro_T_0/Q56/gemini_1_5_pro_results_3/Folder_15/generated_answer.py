def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3 and substring not in substrings:
            substrings.append(substring)
    return substrings