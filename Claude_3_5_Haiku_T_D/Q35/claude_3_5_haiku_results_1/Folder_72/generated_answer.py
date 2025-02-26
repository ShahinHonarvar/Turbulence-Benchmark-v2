def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    chars_count = {}
    for i in range(14, min(len(s) - 1, 70)):
        if s[i] in chars_count:
            chars_count[s[i]] += 1
        else:
            chars_count[s[i]] = 1
    repeat_chars = set((char for char, count in chars_count.items() if count > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) >= 70 or s.index(char) < 14))