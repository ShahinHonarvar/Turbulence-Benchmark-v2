from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    chars = OrderedDict()
    for i, c in enumerate(s):
        if 90 < i < 200 and c in chars:
            chars.pop(c)
        elif 90 <= i < 200:
            chars[c] = None
    return ''.join(chars.keys())