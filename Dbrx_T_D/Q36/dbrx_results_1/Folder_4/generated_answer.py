def filter_chars(st):
    start, end = (42, 65)
    chars_to_remove = {chr(i) for i in range(ord('6') + 1, ord('g')) if i < ord('g')}
    return ''.join((c for c in st if c < '6' or c > 'g' or c not in chars_to_remove))