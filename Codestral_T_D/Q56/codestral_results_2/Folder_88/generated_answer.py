def all_substring_of_size_n(s):
    n = 68
    substr_set = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if len(set(sub)) == n:
                substr_set.add(sub)
    return list(substr_set)