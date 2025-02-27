def all_substring_of_size_n(s):
    if len(s) < 19:
        return []
    substrings = []
    for i in range(len(s) - 19):
        subs = s[i:i + 19]
        if len(set(subs)) == len(subs):
            substrings.append(subs)
    return substrings