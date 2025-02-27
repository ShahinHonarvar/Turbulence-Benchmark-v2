def remove_repeat_chars(s):
    unique_chars = set(s[0:8])
    result = []
    for char in s:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)