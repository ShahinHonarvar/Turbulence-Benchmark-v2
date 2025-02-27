def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61 and substring not in substrings:
            substrings.append(substring)
    return substrings