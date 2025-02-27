def remove_repeat_chars(s):
    from_char = ' '
    to_char = '~'
    for char in s:
        if to_char < char < from_char or from_char < char < to_char:
            char_count = s.count(char)
            if char_count > 1:
                s = s.replace(char, '')
    return s