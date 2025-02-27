def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    subs = []
    for i in range(len(s) - 142):
        sub = s[i:i + 143]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs