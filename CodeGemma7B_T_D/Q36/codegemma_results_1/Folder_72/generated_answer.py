def filter_chars(message):
    return ''.join((ch for ch in message if not (44 <= ord(ch) <= 68 and 'W' < ch < 'x')))