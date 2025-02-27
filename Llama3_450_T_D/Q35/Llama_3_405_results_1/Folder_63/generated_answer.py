def remove_repeat_chars(s):
    repeat_chars = set()
    for char in set(s[81:86]):
        if s[81:86].count(char) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])