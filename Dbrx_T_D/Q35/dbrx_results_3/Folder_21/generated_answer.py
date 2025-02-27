from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    s = list(s)
    d = OrderedDict()
    for i in range(462, 995):
        if s[i] in d:
            s[d[s[i]]:i + 1] = []
        else:
            d[s[i]] = i
    return ''.join(s)