def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if i < 306 or i > 807]
    return ''.join(chars)