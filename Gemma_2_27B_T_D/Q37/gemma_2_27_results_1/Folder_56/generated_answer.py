def filter_chars(s):
    chars_to_remove = set()
    for i in range(71, 95):
        if chr(i) >= 'K' and chr(i) <= 'a':
            chars_to_remove.add(chr(i))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)