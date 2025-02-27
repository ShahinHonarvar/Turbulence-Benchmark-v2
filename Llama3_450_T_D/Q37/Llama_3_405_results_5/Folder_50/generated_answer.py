def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(71, 97) if '_' <= chr(i) <= 'o']
    return ''.join([c for c in s if c not in chars_to_remove])