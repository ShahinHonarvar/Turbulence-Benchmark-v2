def remove_repeat_chars(s):
    chars = s[20:93]
    seen = set()
    repeat = set((c for c in chars if chars.count(c) > 1))
    return ''.join((char for char in s if char not in repeat))