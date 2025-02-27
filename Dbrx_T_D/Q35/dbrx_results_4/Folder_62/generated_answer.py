from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    d = OrderedDict()
    for i in range(len(s)):
        if 50 < i < 92:
            if s[i] not in d:
                d[s[i]] = 1
        else:
            d[s[i]] = 1
    return ''.join(d.keys())