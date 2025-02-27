def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A') + 1, ord('i'))}
    filtered_string = ''.join((c for i, c in enumerate(s) if i <= 27 or i >= 75 or c not in chars_to_remove))
    return filtered_string