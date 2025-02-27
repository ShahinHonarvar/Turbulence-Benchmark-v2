def all_substring_of_size_n(s):
    n = 29
    substrs = {}
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n and len(sub) not in substrs:
            substrs[len(sub)] = [sub]
        elif len(set(sub)) == n and len(sub) in substrs:
            substrs[len(sub)].append(sub)
    return substrs.get(n, [])