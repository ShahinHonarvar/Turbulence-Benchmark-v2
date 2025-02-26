def filter_chars(s):
    chars_to_remove = set()
    for i in range(67, 90):
        char = chr(i)
        if '#' < char < 'T':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))