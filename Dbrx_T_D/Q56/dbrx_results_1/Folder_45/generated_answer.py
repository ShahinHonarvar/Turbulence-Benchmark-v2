def all_substring_of_size_n(s):
    if len(s) < 29:
        return []
    substr = set()
    for i in range(len(s) - 28):
        sub = ''.join(sorted(s[i:i + 29]))
        if len(sub) == 29:
            substr.add(sub)
    return list(substr)