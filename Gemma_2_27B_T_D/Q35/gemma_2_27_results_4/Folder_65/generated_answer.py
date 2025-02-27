def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if i >= 51 and i < 76:
            if s[i] in seen:
                continue
            seen.add(s[i])
        result.append(s[i])
    return ''.join(result)