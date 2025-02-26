def filter_chars(s):
    chars_to_remove = set()
    for i in range(41, 65):
        if i < len(s):
            char = s[i]
            if 'K' <= char <= ']':
                chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result