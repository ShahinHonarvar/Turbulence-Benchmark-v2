def remove_repeat_chars(s):
    mid_part = s[1:6]
    char_count = {char: mid_part.count(char) for char in set(mid_part)}
    result = ''.join((char for char in s if char_count.get(char, 0) <= 1))
    return result