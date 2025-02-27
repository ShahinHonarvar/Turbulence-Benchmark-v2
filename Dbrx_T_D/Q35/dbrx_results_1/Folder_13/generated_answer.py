def remove_repeat_chars(s):
    start, end = (45, 91)
    chars_to_remove = set(s[start:end])
    result = [char for i, char in enumerate(s) if char not in chars_to_remove or i < start or i >= end]
    return ''.join(result)