from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = list(OrderedDict.fromkeys(s[32:44]))
    return s[:32] + ''.join(result) + s[44:]