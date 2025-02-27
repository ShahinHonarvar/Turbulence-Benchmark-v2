from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    start, end = (68, 99)
    char_count = OrderedDict()
    for char in s[start:end]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '', char_count[char] - 1)
    return s