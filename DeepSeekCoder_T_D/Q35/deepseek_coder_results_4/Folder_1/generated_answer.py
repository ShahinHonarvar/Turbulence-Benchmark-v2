def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    sub_str = s[18:88]
    repeat_chars = {char for char, count in Counter(sub_str).items() if count > 1}
    result = s[:18] + ''.join((char for char in s[18:88] if char not in repeat_chars)) + s[88:]
    return result