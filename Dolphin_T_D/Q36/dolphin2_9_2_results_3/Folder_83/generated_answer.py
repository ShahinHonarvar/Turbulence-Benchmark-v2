def filter_chars(s):
    chars_to_remove = [s[i] for i in range(72, 93) if s[i] > '<' and s[i] < 'J']
    for c in chars_to_remove:
        while c in s:
            s = s.replace(c, '', 1)
    return s