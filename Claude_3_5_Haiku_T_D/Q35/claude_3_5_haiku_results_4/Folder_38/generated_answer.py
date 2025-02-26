def remove_repeat_chars(s):
    if len(s) <= 37:
        return s
    slice_str = s[37:85]
    repeated_chars = set((char for char in slice_str if slice_str.count(char) > 1))
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)