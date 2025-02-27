def remove_repeat_chars(s):
    result = []
    seen_chars = set()
    for i in range(10):
        if s[i] in seen_chars:
            continue
        if s[i] in seen_chars or s[i] in result:
            continue
        result.append(s[i])
        seen_chars.add(s[i])
    return ''.join(result)