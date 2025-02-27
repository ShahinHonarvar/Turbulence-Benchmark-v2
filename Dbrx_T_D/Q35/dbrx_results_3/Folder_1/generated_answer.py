def remove_repeat_chars(s):
    start, end = (17, 88)
    chars_to_remove = set(s[start:end])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '', s.count(char) - 1)
    return ''.join(sorted(s, key=lambda x: (s.index(x) >= start) - (s.index(x) > end), reverse=True))