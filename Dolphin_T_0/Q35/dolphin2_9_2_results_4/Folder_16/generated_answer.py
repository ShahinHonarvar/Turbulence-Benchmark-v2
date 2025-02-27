def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[90:97]:
        if s.count(char) > 1:
            repeat_chars.add(char)
    return ''.join([c for c in s if c not in repeat_chars])