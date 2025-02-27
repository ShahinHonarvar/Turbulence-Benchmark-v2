def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 46):
        sub = s[i:i + 47]
        if len(set(sub)) == 47:
            subs.append(sub)
    return subs