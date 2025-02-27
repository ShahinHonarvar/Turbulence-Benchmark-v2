from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    ordered_dict = OrderedDict()
    start, end = (13, 76)
    for i in range(start, end):
        if s[i] in ordered_dict:
            ordered_dict[s[i]] = None
        else:
            ordered_dict[s[i]] = s[i]
    result = ''.join(filter(lambda x: x is not None, ordered_dict.values()))
    return s[:start] + result + s[end:]