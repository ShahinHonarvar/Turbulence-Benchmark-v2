def all_substring_of_size_n(s):
    n = 120
    subs = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if len(sub) == n and len(set(sub)) == n:
                if sub not in subs:
                    subs.append(sub)
    return subs