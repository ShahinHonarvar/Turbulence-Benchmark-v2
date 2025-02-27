def remove_repeat_chars(s):
    result = ''
    repeat_chars = []
    for i in range(32, 99):
        if s.count(chr(i)) > 1 and chr(i) not in repeat_chars:
            repeat_chars.append(chr(i))
    for char in s:
        if char not in repeat_chars:
            result += char
    return result