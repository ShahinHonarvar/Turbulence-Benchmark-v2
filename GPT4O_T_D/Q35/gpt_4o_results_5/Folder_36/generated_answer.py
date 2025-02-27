def remove_repeat_chars(s):
    if len(s) < 709:
        return s
    sub = s[477:709]
    repeat_chars = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or not 477 < s.index(char) < 709))