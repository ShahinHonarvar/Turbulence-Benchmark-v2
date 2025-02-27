from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:

    def remove_char_at_index(s: str, index: int) -> str:
        return s[:index] + s[index + 1:]
    s = s[1:9]
    unique_chars = OrderedDict()
    for char in s:
        if char in unique_chars:
            s = remove_char_at_index(s, unique_chars[char])
        else:
            unique_chars[char] = s.index(char)
    return s