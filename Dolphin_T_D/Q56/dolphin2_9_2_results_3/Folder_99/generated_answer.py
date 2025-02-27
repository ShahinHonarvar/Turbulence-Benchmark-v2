def all_substring_of_size_n(s):
    n = len(s)
    subs = []
    for i in range(n):
        for j in range(i + 1, n):
            if len(set(s[i:j + 1])) == 110 and len(set(s[i:j + 1])) == j - i + 1:
                subs.append(''.join(sorted(s[i:j + 1])))
    return list(set(subs))