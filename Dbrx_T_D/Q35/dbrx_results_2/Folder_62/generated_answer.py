from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = list(OrderedDict.fromkeys(s[50:92]))
    return s[:50] + ''.join(result) + s[92:]