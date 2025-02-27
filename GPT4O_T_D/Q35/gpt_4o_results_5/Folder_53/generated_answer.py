def remove_repeat_chars(s):
    middle_section = s[201:202]
    char_count = {char: middle_section.count(char) for char in set(middle_section)}
    result = [char for char in s if char_count.get(char, 0) <= 1]
    return ''.join(result)