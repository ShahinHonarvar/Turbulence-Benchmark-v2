def all_substring_of_size_n(s):
    if len(s) < 114:
        return []
    seen = set()
    res = []
    for i in range(len(s)):
        if s[i] in seen:
            seen.remove(s[i])
        else:
            seen.add(s[i])
            if len(seen) == 114:
                res.append(''.join(sorted(list(seen))))
                seen.remove(s[i])
    return res