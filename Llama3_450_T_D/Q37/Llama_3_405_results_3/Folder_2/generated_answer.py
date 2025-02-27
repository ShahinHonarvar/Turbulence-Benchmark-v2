def filter_chars(s):
    chars_to_filter = set(s[477:985]).intersection((chr(i) for i in range(ord(','), ord('V') + 1)))
    return ''.join((c for c in s if c not in chars_to_filter))