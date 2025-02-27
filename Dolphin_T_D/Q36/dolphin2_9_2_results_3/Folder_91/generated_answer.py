def filter_chars(string):
    chars_to_remove = []
    for i in range(1, 3):
        if '!' < string[i] < '#':
            chars_to_remove.append(string[i])
    return ''.join([ch for ch in string if ch not in chars_to_remove])