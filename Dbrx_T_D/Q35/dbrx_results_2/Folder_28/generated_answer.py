def remove_repeat_chars(s):
    result = ''
    seen = set()
    for i in range(len(s)):
        if i >= 86 and i < 99:
            if s[i] in seen:
                continue
            else:
                seen.add(s[i])
        result += s[i]
    return result