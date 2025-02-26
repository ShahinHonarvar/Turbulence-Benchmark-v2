def filter_chars(s):
    if len(s) <= 33:
        return s
    chars_to_remove = set()
    for i in range(19, 31):
        if 'H' < s[i] < '|':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result