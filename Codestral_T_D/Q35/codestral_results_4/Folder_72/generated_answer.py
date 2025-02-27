def remove_repeat_chars(string):
    chars = string[13:70]
    repeats = [char for char in chars if chars.count(char) > 1]
    unique_repeats = set(repeats)
    result = ''.join([char for char in string if char not in unique_repeats])
    return result