def remove_repeat_chars(s):
    chars = []
    for i in range(len(s)):
        if 6 <= i < 9:
            if s[i] not in chars:
                chars.append(s[i])
        else:
            chars.append(s[i])
    return ''.join(chars)