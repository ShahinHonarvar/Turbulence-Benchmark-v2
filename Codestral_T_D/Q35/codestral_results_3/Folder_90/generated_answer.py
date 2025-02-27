def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[306:807] if s[306:807].count(char) > 1])
    altered_string = ''.join([char for char in s if char not in repeat_chars])
    return altered_string