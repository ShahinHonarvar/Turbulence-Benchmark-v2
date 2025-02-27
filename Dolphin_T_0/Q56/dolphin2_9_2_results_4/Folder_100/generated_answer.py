def all_substring_of_size_n(s):
    if len(s) < 92:
        return []
    ss = set()
    for i in range(len(s) - 91):
        if len(set(s[i:i + 92])) == 92:
            ss.add(s[i:i + 92])
    return list(ss)