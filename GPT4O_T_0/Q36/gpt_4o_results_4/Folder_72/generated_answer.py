def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('W') + 1, ord('x'))}
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or not 44 < s.index(c) < 68))
    return filtered_string