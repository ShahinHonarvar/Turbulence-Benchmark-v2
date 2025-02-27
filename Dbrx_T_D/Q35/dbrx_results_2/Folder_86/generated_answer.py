from collections import OrderedDict

def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(19, 33):
        if s[i] in chars_to_remove:
            s = s[:i] + s[i + 1:]
        else:
            chars_to_remove.add(s[i])
    return ''.join(OrderedDict.fromkeys(s))