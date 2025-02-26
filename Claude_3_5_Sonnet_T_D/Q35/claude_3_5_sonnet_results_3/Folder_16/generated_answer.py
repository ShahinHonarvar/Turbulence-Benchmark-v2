def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    target_slice = s[91:97]
    repeat_chars = set((char for char in target_slice if target_slice.count(char) > 1))
    result = []
    for i, char in enumerate(s):
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)