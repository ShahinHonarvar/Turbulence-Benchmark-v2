def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A') + 1, ord('i'))}
    filtered_string = ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or i <= 27 or i >= 75))
    return filtered_string