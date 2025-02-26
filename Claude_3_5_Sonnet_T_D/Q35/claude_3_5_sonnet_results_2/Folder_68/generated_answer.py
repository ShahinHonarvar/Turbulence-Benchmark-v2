def remove_repeat_chars(s):
    first_ten = s[1:10]
    repeat_chars = set((char for char in first_ten if first_ten.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))