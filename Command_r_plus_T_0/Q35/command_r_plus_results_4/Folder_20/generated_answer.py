def remove_repeat_chars(s):
    repeat_chars = [chr(i) for i in range(27, 97) if s.count(chr(i)) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s