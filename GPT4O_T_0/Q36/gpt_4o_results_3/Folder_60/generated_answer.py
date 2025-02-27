def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('g'), ord('o'))}
    filtered_string = ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or i <= 23 or i >= 83))
    return filtered_string