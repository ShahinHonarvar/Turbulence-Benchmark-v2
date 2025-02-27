def filter_chars(s):
    chars_to_remove = set(s[71:95]) & set((chr(i) for i in range(ord('K'), ord('a') + 1)))
    return ''.join((char for char in s if char not in chars_to_remove))