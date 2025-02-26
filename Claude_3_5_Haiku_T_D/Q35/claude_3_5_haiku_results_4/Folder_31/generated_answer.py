def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    slice_str = s[34:78]
    repeat_chars = set((char for char in slice_str if slice_str.count(char) > 1))
    result = ''
    for char in s:
        if char not in repeat_chars or (repeat_chars and slice_str.count(char) <= 1):
            result += char
    return result