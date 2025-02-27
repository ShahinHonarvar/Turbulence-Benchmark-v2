def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            if substring not in substrings:
                substrings.append(substring)
    return substrings