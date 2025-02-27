def remove_repeat_chars(s):
    start, end = (476, 709)
    sub_s = s[start:end]
    repeat_chars = {char for char, count in Counter(sub_s).items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result