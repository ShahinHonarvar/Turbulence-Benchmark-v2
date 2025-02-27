def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(20, 43):
        if s[i] in seen:
            continue
        seen.add(s[i])
        result.append(s[i])
    return ''.join(result)