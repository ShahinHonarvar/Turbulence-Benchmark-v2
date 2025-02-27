def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 16):
        si = s[i:i + 17]
        if len(set(si)) == len(si):
            subs.add(si)
    return list(subs)