def remove_repeat_chars(s):
    chars = s[46:91]
    seen = set()
    repeat = set((char for char in chars if chars.count(char) > 1))
    return ''.join((c for c in s if c not in repeat))