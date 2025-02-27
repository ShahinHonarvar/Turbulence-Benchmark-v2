def remove_repeat_chars(s):
    seen = {x: 1 for x in s[27:96]}
    result = []
    for c in s:
        if not (27 <= len(result) <= 96 and c in seen):
            result.append(c)
            seen[c] = seen.get(c, 0) + 1
    return ''.join(result)