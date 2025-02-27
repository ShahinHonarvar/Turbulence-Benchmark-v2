def filter_chars(text):
    chars_to_remove = set()
    for i in range(71, 97):
        if chr(i) >= '_' and chr(i) <= 'o':
            chars_to_remove.add(chr(i))
    result = ''.join([c for c in text if c not in chars_to_remove])
    return result