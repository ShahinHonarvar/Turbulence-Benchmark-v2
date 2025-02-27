def filter_chars(s):
    chars_to_remove = [chr(c) for c in range(ord('m'), ord('w') + 1)]
    return ''.join([char for i, char in enumerate(s) if not (25 <= i <= 97 and char in chars_to_remove)])