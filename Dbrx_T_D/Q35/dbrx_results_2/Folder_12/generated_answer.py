from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    substr = s[16:87]
    unique_substr = list(OrderedDict.fromkeys(substr))
    return ''.join((c for c in s if c not in unique_substr or s.index(c) < 16 or s.index(c) >= 87))