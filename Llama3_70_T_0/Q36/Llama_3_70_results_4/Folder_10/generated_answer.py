def filter_chars(s):
    chars_to_remove = set()
    for char in s[35:60]:
        if '!' < char < 'B':
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])