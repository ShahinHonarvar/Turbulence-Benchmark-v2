def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 32 < i < 44 and s[i] in s[33:43]:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result += char
    return result