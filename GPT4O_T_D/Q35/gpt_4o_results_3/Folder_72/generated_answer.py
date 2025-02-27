def remove_repeat_chars(s):
    sub_str = s[14:70]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars or char in s[:14] or char in s[70:]))
    return result