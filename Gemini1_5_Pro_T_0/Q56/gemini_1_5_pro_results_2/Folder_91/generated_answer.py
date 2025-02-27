def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6 and substring not in substrings:
            substrings.append(substring)
    return substrings