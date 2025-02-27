def all_substring_of_size_n(s):
    length = len(s)
    subs = []
    if length < 31:
        return subs
    for i in range(length - 29):
        sub = s[i:i + 31]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs