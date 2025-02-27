def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[125:825]:
        if s[125:825].count(char) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])