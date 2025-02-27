def remove_repeat_chars(s):
    repeat_chars = [char for i, char in enumerate(s) if s.count(char, 86, 89) > 1 and 86 <= i < 89]
    return ''.join([char for char in s if char not in repeat_chars])