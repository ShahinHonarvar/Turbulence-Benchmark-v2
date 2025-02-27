def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s:
        if s.index(c) < 10 and c in s[s.index(c) + 1:10] and (c not in seen):
            seen.add(c)
        else:
            result.append(c)
    return ''.join(result)