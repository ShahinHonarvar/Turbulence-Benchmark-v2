def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if 2 <= i < 8 and s[i] in seen:
            continue
        if 2 <= i < 8:
            seen.add(s[i])
        result.append(s[i])
    return ''.join(result)