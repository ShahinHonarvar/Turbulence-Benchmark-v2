def filter_chars(s):
    chars_to_remove = []
    for i in range(124, 855):
        if '9' <= s[i] <= 's':
            chars_to_remove.append(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])