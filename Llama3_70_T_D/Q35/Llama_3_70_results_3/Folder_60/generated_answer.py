def remove_repeat_chars(s):
    slice_ = s[38:52]
    for char in set(slice_):
        if slice_.count(char) > 1:
            s = s.replace(char, '')
    return s