def filter_chars(s):
    chars_to_remove = []
    for i in range(154, 222):
        if i < len(s):
            char = s[i]
            if char > 'A' and char < 'f':
                chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s