def remove_repeat_chars(s):
    seen = set()
    repeat_chars = set()
    for char in s[56:88]:
        if char in seen:
            repeat_chars.add(char)
        seen.add(char)
    return ''.join((char for char in s if char not in repeat_chars))