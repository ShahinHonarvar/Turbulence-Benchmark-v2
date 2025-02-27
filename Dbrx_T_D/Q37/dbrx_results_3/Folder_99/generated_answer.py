def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('T'), ord('h') + 1) if 373 <= i <= 901}
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)