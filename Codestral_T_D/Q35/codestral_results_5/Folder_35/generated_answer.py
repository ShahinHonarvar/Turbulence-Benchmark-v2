def remove_repeat_chars(s):
    substring = s[77:84]
    chars_to_remove = {c for c in substring if substring.count(c) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))