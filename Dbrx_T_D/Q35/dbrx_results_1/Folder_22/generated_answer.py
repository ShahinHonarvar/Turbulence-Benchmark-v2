from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = s[:50] + ''.join(OrderedDict.fromkeys(s[50:200])) + s[200:]
    return result