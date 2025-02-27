def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 16):
        subs_of_size_17 = s[i:i + 17]
        if len(set(subs_of_size_17)) == 17:
            subs.append(subs_of_size_17)
    return subs