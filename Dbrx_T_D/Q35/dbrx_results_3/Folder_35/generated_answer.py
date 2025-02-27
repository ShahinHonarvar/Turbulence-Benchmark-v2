from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(77, 84):
        if s[i] in s[i + 1:84] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return ''.join(OrderedDict.fromkeys(s))