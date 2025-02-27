def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(61, 200):
        if i in range(len(s)):
            c = s[i]
            if c in seen:
                repeated.add(c)
            seen.add(c)
    result = []
    for c in s:
        if c not in repeated:
            result.append(c)
    return ''.join(result)