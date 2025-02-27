def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 78):
        if len(set(s[i:i + 79])) == 79:
            subs.append(s[i:i + 79])
    if len(subs) == 0:
        return []
    return subs