def remove_repeat_chars(s):
    chars = s[306:807]
    seen = set()
    repeat = set((char for char in chars if chars.count(char) > 1))
    return ''.join((char for char in s if char not in repeat))