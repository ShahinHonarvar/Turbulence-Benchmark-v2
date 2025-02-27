def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('5'), ord('<') + 1) if 24 <= i <= 82}
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result