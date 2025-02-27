def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 88 + 1):
        substring = s[i:i + 88]
        if len(set(substring)) == 88 and substring not in substrings:
            substrings.append(substring)
    return substrings