def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(0, 10):
        if s[i] not in seen:
            result.append(s[i])
            seen.add(s[i])
        elif s[i] in seen:
            pass
    return ''.join(result)