def remove_repeat_chars(in_str):
    return ''.join([char for char in in_str if not in_str[36:52].count(char) > 1])