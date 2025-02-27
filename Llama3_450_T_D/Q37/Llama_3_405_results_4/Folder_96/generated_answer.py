def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(86, 93) if '!' <= chr(i) <= 's']
    return ''.join((c for c in s if c not in chars_to_remove))