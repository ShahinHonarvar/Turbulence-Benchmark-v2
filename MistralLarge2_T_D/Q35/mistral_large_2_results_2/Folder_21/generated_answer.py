def remove_repeat_chars(s):
    sub_s = s[463:995]
    repeat_chars = {char for char in sub_s if sub_s.count(char) > 1}
    result = ''.join([char for char in s if char not in repeat_chars])
    return result