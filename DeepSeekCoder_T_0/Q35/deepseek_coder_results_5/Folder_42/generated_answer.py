def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    sub_str = s[18:60]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = s[:18] + ''.join((char for char in s[18:60] if char not in repeat_chars)) + s[60:]
    return result