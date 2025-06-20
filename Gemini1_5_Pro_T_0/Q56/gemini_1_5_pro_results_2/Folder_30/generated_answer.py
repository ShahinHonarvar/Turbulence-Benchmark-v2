def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 78):
        substring = s[i:i + 79]
        if len(set(substring)) == 79 and substring not in substrings:
            substrings.append(substring)
    return substrings