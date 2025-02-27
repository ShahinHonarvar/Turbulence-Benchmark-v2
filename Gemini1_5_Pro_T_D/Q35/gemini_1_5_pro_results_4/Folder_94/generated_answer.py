def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 42 < i < 87:
            if char in seen_chars:
                continue
            elif s[42:87].count(char) > 1:
                seen_chars.add(char)
                continue
        result += char
    return result