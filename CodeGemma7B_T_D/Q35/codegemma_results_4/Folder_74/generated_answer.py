def remove_repeat_chars(s):
    if len(s) < 69 or len(s) > 97:
        return s
    else:
        seen_chars = set()
        result = ''
        for i in range(69, 97):
            if s[i] in seen_chars:
                continue
            seen_chars.add(s[i])
            result += s[i]
        return result