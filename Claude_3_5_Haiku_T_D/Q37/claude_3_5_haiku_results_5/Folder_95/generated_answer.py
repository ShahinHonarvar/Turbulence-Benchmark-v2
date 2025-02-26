def filter_chars(s):
    indices_to_filter = list(range(35, 41))
    chars_to_remove = set()
    for i in indices_to_filter:
        if i < len(s) and ')' <= s[i] <= 'l':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))