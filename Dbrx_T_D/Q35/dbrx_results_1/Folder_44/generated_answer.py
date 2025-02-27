from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    ord_dict = OrderedDict()
    for i in range(len(s)):
        if 36 < i < 52:
            if s[i] in ord_dict:
                continue
            else:
                ord_dict[s[i]] = 1
        else:
            ord_dict[s[i]] = 1
    return ''.join(ord_dict.keys())