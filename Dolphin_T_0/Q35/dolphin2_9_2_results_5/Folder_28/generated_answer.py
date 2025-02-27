def remove_repeat_chars(string):
    repeat_chars = [ch for ch in string[86:99] if string.count(ch) > 1]
    for ch in repeat_chars:
        string = string.replace(ch, '')
    return string