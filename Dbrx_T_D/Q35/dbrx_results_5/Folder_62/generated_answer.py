from collections import OrderedDict

def remove_repeat_chars(s):
    if len(s) < 50 or len(s) < 92:
        return s
    unique_chars = list(OrderedDict.fromkeys(s[50:92]))
    for char in unique_chars:
        s = s.replace(char, '', s[50:92].count(char))
    return s