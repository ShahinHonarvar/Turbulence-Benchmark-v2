def remove_repeat_chars(string):
    substring = string[86:99]
    repeat_chars = [char for char in substring if substring.count(char) > 1]
    altered_string = ''.join([char for char in string if char not in repeat_chars])
    return altered_string