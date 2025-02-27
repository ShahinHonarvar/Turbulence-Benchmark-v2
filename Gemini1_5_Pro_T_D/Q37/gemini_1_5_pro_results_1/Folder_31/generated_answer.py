def filter_chars(s):
    chars_to_remove = []
    for i in range(57, 97):
        if i >= ord('<') and i <= ord('w') and (s[i:i + 1] in s):
            chars_to_remove.append(s[i:i + 1])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s