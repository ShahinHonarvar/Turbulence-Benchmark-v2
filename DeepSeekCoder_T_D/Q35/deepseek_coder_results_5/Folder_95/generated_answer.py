def remove_repeat_chars(s):
    sub_str = s[32:99]
    repeat_chars = {char for char, count in Counter(sub_str).items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result