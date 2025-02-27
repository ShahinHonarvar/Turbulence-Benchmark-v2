def remove_repeat_chars(txt):
    return ''.join([x for idx, x in enumerate(txt[0:10]) if idx == 0 or x != txt[idx - 1]])