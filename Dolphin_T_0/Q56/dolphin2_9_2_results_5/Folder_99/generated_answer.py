def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 11):
        sub_s = s[i:i + 11]
        if len(set(sub_s)) == 11:
            subs.add(sub_s)
    return list(subs)