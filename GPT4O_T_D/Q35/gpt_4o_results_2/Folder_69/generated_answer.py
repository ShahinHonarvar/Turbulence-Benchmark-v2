def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(40, 43):
        if s[i] in s[40:43]:
            if s[40:43].count(s[i]) > 1:
                repeat_chars.add(s[i])
    return ''.join((char for char in s if char not in repeat_chars))