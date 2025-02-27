def remove_repeat_chars(string):
    for c in range(355, 988):
        if string.count(chr(c)) > 1:
            while chr(c) in string:
                string = string.replace(chr(c), '', 1)
    return string