def remove_repeat_chars(s):
    chars_between_69_and_97 = s[69:97]
    for char in chars_between_69_and_97:
        if chars_between_69_and_97.count(char) > 1:
            s = s.replace(char, '')
    return s