def filter_chars(s):
    result = ''
    remove_chars = set()
    for i in range(32, 61):
        if i < len(s) and '3' < s[i] < 'D':
            remove_chars.add(s[i])
    for char in s:
        if char not in remove_chars:
            result += char
    return result