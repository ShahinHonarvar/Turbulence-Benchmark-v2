def remove_repeat_chars(s):
    repeating_chars = set()
    for char in set(s[20:36]):
        if s[20:36].count(char) > 1:
            repeating_chars.add(char)
    return ''.join([char for char in s if char not in repeating_chars])