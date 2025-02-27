def all_substring_of_size_n(s):
    if len(s) < 105:
        return []
    substrings = []
    for i in range(len(s) - 104):
        sub = s[i:i + 105]
        if len(set(sub)) == 105:
            substrings.append(sub)
            while sub in s[i + 1:]:
                i += 1
    return substrings