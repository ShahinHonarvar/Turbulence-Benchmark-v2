def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s)):
        for j in range(i + 33, len(s) + 1):
            if len(set(s[i:j])) == 33:
                subs.append(s[i:j])
    return subs