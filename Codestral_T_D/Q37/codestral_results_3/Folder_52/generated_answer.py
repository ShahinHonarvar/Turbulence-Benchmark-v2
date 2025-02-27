def filter_chars(s):
    chars_to_remove = [chr(c) for c in range(ord('j'), ord('v') + 1)]
    return ''.join((c for i, c in enumerate(s) if not (54 <= i <= 83 and c in chars_to_remove)))