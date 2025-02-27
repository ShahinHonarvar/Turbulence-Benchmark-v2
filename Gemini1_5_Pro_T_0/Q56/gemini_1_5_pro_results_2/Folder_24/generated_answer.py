def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52 and substring not in substrings:
            substrings.append(substring)
    return substrings