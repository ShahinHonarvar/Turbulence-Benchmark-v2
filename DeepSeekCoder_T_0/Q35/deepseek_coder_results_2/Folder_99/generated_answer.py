def remove_repeat_chars(s):
    start, end = (450, 905)
    sub_str = s[start:end]
    repeat_chars = {char for char, count in Counter(sub_str).items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result