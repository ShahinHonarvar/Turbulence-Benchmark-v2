def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    sub_str = s[10:100]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = s[:10] + ''.join((char for char in s[10:] if char not in repeat_chars))
    return result