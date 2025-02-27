from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    result = s[32:99].strip()
    char_count = OrderedDict(((char, result.count(char)) for char in set(result)))
    for char, count in char_count.items():
        if count > 1:
            result = result.replace(char, '', count - 1)
    return s[:32] + result + s[99:]