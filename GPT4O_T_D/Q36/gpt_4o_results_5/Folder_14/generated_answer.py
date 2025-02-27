def filter_chars(s):
    result = []
    chars_to_remove = set()
    for i in range(42, 56):
        if i < len(s) and 'Z' < s[i] < 'c':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)