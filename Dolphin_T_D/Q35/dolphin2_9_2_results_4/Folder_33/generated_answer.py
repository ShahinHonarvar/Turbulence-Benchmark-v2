def remove_repeat_chars(s):
    chars_between_125_and_825 = s[125:825]
    repeat_chars = [char for char in chars_between_125_and_825 if chars_between_125_and_825.count(char) > 1]
    for char in repeat_chars:
        s = ''.join([c for c in s if c != char])
    return s