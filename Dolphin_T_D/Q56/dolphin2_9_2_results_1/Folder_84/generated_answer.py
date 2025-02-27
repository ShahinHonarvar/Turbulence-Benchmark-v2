def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 113):
        if len(set(s[i:i + 114])) == 114:
            subs.add(s[i:i + 114])
    return list(subs)