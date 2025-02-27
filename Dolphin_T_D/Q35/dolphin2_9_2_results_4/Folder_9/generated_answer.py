def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[80:200]:
        if s.count(char) > 1:
            repeat_chars.add(char)
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s