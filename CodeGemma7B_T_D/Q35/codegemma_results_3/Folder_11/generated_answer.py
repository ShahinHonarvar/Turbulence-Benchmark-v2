def remove_repeat_chars(s):
    seen = set()
    res = []
    for i in range(len(s)):
        if i < 48 or i >= 76 or s[i] in seen:
            continue
        seen.add(s[i])
        res.append(s[i])
    return ''.join(res)