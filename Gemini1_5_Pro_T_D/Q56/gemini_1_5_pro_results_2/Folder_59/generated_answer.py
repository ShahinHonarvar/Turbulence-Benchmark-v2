def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 77 + 1):
        substring = s[i:i + 77]
        if len(set(substring)) == 77 and substring not in substrings:
            substrings.append(substring)
    return substrings