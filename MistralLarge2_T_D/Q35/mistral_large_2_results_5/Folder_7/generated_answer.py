def remove_repeat_chars(s):
    substring = s[375:926]
    char_count = {char: substring.count(char) for char in set(substring)}
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s