def remove_repeat_chars(string):
    new_line_string = string[0:60] + ''.join(dict.fromkeys(string[60:200])) + string[200:]
    return new_line_string