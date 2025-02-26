def filter_chars(s):
    filtered_chars = []
    chars_to_remove = set()
    for i in range(55, 80):
        if i < len(s) and 'S' < s[i] < 's':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            filtered_chars.append(char)
    return ''.join(filtered_chars)