def filter_chars(s):
    chars_to_remove = set()
    for i in range(91, 97):
        if 'j' < chr(i) < 'w':
            chars_to_remove.add(chr(i))
    return ''.join((char for char in s if char not in chars_to_remove))