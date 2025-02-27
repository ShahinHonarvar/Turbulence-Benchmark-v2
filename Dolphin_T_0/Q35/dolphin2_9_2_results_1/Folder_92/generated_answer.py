def remove_repeat_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[:2], start=1) if s.find(c) != s.rfind(c)]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s