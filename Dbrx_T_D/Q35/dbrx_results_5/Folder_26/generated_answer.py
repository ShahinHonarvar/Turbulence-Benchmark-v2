def remove_repeat_chars(s):
    chars = list(s)
    for i in range(68, 99):
        if chars[i] in chars[i + 1:] + chars[:i]:
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)