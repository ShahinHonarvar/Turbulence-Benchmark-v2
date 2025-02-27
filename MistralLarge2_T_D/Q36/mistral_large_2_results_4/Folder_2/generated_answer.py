def filter_chars(s):
    chars_to_remove = set()
    for index in range(422, 854):
        if index < len(s) and 'D' < s[index] < 'J':
            chars_to_remove.add(s[index])
    return ''.join((char for char in s if char not in chars_to_remove))