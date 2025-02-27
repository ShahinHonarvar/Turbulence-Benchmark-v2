def filter_chars(s):
    chars_to_filter = [chr(i) for i in range(26, 65) if 'V' <= chr(i) <= 'o']
    return ''.join((c for c in s if c not in chars_to_filter))