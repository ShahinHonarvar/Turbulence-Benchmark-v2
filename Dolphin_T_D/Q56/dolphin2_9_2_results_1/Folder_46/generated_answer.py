def all_substring_of_size_n(s):
    if len(set(s)) == len(s):
        subs = [s[i:i + 87] for i in range(len(s) - 86)]
        subs = [x for x in subs if len(set(x)) == 87]
        return subs
    return []