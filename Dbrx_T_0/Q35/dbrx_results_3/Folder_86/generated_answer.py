from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = s[:19] + ''.join(OrderedDict.fromkeys(s[19:33])) + s[33:]
    return result