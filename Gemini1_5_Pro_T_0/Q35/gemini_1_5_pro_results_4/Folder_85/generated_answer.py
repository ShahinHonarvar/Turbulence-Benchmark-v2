def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 1 < i < 8 and c in s[2:i]:
            if c not in seen:
                seen.add(c)
                result = result[:result.rfind(c)]
        else:
            result += c
    return result