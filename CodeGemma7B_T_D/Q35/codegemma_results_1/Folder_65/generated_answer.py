def remove_repeat_chars(s):
    result = []
    seen = set()
    for i in range(len(s)):
        if i >= 51 and i < 76:
            if s[i] not in seen:
                seen.add(s[i])
                result.append(s[i])
    return ''.join(result)