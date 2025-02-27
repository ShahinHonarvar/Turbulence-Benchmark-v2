def remove_repeat_chars(s):
    middle_part = s[3:8]
    to_remove = {char for char in middle_part if middle_part.count(char) > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result