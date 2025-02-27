def remove_repeat_chars(str):
    return ''.join([c for i, c in enumerate(str) if i < 73 or i > 84 or str.count(c) <= 1])