def all_substring_of_size_n(s):
    if len(s) < 92:
        return []
    sublists = []
    for i in range(len(s)):
        sub = s[i:i + 92]
        if len(set(sub)) == 92:
            sublists.append(sub)
    return sublists