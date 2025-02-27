def remove_repeat_chars(s):
    chars_between_35_and_64 = [s[i] for i in range(35, 65) if s[i] not in s[65:]]
    for char in chars_between_35_and_64:
        s = s.replace(char, '')
    return s