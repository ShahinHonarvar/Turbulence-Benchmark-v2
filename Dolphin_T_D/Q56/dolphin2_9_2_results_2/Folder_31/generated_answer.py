def all_substring_of_size_n(s):
    n = 46
    subs = set()
    for i in range(len(s)):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            subs.add(substr)
    return list(subs)