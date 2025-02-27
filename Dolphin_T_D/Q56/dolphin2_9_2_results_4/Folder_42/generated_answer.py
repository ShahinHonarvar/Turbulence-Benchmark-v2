def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n - 44):
        sub_set = {s[i + j] for j in range(45)}
        if len(sub_set) == 45:
            subs.add(''.join(sub_set))
    return list(subs)