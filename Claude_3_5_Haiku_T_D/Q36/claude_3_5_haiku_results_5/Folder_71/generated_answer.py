def filter_chars(s):
    filtered_chars = []
    chars_to_remove = []
    for i in range(83, 89):
        if '*' < s[i] < '[':
            chars_to_remove.append(s[i])
    for char in s:
        if char not in chars_to_remove:
            filtered_chars.append(char)
    return ''.join(filtered_chars)