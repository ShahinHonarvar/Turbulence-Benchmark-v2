def remove_repeat_chars(s):
    chars = [c for c in s]
    for c in chars:
        if s.count(c) > 1 and 69 < s.index(c) < 97:
            chars = [x for x in chars if x != c]
    return ''.join(chars)