def all_substring_of_size_n(s):
    if len(set(s)) < 39:
        return []
    substrings = []
    for i in range(len(s) - 38):
        sub = s[i:i + 39]
        if len(set(sub)) == 39 and sub not in substrings:
            substrings.append(sub)
    return substrings