def remove_repeat_chars(s):
    result = []
    seen = set()
    for i in range(len(s)):
        if 32 < i < 99 and s[i] in seen:
            continue
        result.append(s[i])
        seen.add(s[i])
    return ''.join(result)