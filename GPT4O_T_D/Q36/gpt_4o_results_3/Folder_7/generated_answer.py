def filter_chars(s):
    if len(s) <= 502:
        return s
    filtered_chars = {chr(i) for i in range(ord('W') + 1, ord('y'))}
    chars_to_remove = set(s[503:946]) & filtered_chars
    return ''.join((c for c in s if c not in chars_to_remove))