def filter_chars(s):
    chars_to_remove = set()
    for i in range(324, 526):
        if ')' < s[i] < 'O':
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result