from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    s = s[:38] + ''.join(OrderedDict.fromkeys(s[38:81])) + s[81:]
    return ''.join((c for c in s if s.count(c) == 1 or (38 <= s.index(c) < 81 and s.count(c) == 1) or (s.index(c) >= 81 and s.count(c) > 1)))