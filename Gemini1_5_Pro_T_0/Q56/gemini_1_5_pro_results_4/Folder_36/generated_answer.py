def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 145):
        substring = s[i:i + 146]
        if len(set(substring)) == 146 and substring not in substrings:
            substrings.append(substring)
    return substrings