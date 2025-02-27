def all_substring_of_size_n(s):
    n = 106
    subs = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            subs.add(substring)
    return list(subs)