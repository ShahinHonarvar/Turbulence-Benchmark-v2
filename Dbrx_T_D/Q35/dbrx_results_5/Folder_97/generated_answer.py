from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    substr = s[34:69]
    ord_dict = OrderedDict.fromkeys(substr)
    for char in ord_dict.keys():
        if substr.count(char) > 1:
            s = s.replace(char, '', substr.count(char))
    return s