def filter_chars(s):
    filtered_chars = set()
    for i in range(71, 97):
        if chr(i) >= '_' and chr(i) <= 'o':
            filtered_chars.add(chr(i))
    for char in filtered_chars:
        s = s.replace(char, '')
    return s