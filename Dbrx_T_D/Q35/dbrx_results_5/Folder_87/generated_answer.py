def remove_repeat_chars(s):
    used_chars = set()
    result = ''
    for i in range(len(s)):
        if i < 20 or i >= 43 or s[i] not in used_chars:
            result += s[i]
            if s[i] != ' ':
                used_chars.add(s[i])
    return result