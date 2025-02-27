def remove_repeat_chars(s):
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i < 56 or i >= 88:
            result.append(s[i])
            used_chars.add(s[i])
        elif s[i] not in used_chars:
            result.append(s[i])
            used_chars.add(s[i])
    return ''.join(result)