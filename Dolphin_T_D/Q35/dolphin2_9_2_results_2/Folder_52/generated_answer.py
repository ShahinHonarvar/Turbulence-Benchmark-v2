def remove_repeat_chars(s):
    char_index = dict()
    for ind, char in enumerate(s):
        if 38 < ind < 81:
            if char_index.get(char) is not None:
                s = s.replace(char, '')
    return s