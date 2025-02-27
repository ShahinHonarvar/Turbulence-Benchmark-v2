def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    sub_str = s[1:8]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = s[0] + ''.join((char for char in s[1:-1] if char not in repeat_chars)) + s[-1]
    return result