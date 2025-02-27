def filter_chars(s):
    chars_to_remove = set(s[19:23])
    filtered_chars = {chr(i) for i in range(ord(']'), ord('t') + 1)}
    chars_to_remove = chars_to_remove & filtered_chars
    return ''.join((c for c in s if c not in chars_to_remove))