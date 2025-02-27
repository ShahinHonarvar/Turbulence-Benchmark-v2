def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 26):
        if len(set(s[i:i + 27])) == 27:
            subs.add(s[i:i + 27])
    return list(subs)