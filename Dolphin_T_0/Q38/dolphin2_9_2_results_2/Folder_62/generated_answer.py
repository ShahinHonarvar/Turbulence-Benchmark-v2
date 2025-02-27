def find_subset_of_length_n(s):
    if len(s) < 86:
        return 0
    subs = []
    for i in range(len(s)):
        subs.append(s[i])
    return len(subs)