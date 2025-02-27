def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 21):
        sub = s[i:i + 22]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs