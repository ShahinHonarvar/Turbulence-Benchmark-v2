def remove_repeat_chars(s):
    between_450_905 = s[450:905]
    unique_chars = set(between_450_905)
    to_remove = [char for char in unique_chars if between_450_905.count(char) > 1]
    for to_remove_char in to_remove:
        s = s.replace(to_remove_char, '')
    return s