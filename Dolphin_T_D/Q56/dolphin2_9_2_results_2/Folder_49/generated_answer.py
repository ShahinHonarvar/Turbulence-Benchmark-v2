def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 6):
        if len(set(s[i:i + 7])) == 7:
            subs.append(s[i:i + 7])
    subs = list(set(subs))
    return subs