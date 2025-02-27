def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 57):
        substring = s[i:i + 58]
        if len(set(substring)) == 58 and substring not in substrings:
            substrings.append(substring)
    return substrings