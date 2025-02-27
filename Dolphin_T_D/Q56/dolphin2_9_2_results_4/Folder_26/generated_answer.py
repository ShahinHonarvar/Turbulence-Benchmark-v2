def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == 3 and sub not in subs:
            subs.append(sub)
    return subs