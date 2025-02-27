def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i in range(2, 8):
        if s[i] in seen_chars:
            continue
        seen_chars.add(s[i])
        result.append(s[i])
    return ''.join(result)