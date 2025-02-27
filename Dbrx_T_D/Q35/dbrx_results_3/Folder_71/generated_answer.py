from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    if len(s) < 36:
        return ''.join(OrderedDict.fromkeys(s))
    s = list(OrderedDict.fromkeys(s))
    for i in range(20, 35):
        if s[i] in s[35:]:
            s[i] = None
    return ''.join(filter(None, s))