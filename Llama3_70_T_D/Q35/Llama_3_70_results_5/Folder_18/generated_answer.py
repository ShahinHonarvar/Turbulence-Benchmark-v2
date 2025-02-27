def remove_repeat_chars(s):
    temp = s[56:90]
    repeat_chars = [char for char in set(temp) if temp.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])