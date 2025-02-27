def all_substring_of_size_n(s):
    n = 23
    subs = set()
    for i in range(len(s) - n + 1):
        subs.add(s[i:i + n])
    subs = list(subs)
    result = []
    for i in subs:
        if len(set(i)) == n:
            result.append(i)
    return result