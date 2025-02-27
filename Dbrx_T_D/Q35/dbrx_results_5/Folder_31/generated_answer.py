def remove_repeat_chars(s):
    chars_between_33_and_78 = set(s[32:78])
    for char in chars_between_33_and_78:
        if s[32:78].count(char) > 1:
            s = s.replace(char, '', s[32:78].index(char) + 33)
    return s