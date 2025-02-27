def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if 48 <= i < 76:
            if s[i] not in seen:
                seen.add(s[i])
            else:
                s = s[:i] + s[i + 1:]
                i -= 1
        else:
            result.append(s[i])
    return ''.join(result)