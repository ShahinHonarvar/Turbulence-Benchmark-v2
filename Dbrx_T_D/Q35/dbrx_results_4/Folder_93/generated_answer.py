from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    s = list(s)
    for i in range(57, 85):
        if s[i] in s[i + 1:]:
            s = list(OrderedDict.fromkeys(s[:i + 1]))
    return ''.join(s)