def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 25):
        sub = s[i:i + 25]
        if len(set(sub)) == len(sub) and sub not in substrings:
            substrings.append(sub)
    return substrings