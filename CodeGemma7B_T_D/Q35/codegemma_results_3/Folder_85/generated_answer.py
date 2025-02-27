def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[1:9], start=1):
        if i <= 8 and c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)