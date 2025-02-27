from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = s[:18] + ''.join(OrderedDict.fromkeys(s[18:60])) + s[60:]
    return result