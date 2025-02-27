def remove_repeat_chars(s):
    if len(s) <= 410:
        return s
    substring = s[410:502]
    chars_to_remove = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 410 or s.index(char) >= 502))