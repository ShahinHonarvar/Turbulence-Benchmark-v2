def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 54):
        sub = s[i:i + 55]
        if len(set(sub)) == 55:
            subs.append(sub)
    return subs