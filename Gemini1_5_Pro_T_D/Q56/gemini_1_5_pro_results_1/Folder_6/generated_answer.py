def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if len(set(substring)) == 23 and substring not in substrings:
            substrings.append(substring)
    return substrings