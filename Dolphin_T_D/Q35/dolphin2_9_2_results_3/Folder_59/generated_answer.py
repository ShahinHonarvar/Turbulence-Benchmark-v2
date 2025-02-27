def remove_repeat_chars(s):
    chars_between_0_and_10 = s[:11]
    unique_chars = set(chars_between_0_and_10)
    to_remove = [char for char in unique_chars if chars_between_0_and_10.count(char) > 1]
    for char in to_remove:
        s = s.replace(char, '')
    return s