def filter_chars(s):
    chars_to_remove = set(s[343:665]).intersection(set([chr(i) for i in range(ord('%') + 1, ord('U'))]))
    return ''.join([char for char in s if char not in chars_to_remove])