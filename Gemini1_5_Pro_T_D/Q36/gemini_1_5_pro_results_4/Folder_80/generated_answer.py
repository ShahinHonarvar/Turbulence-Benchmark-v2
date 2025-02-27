def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 92):
        if i >= len(s):
            break
        if s[i] > 'J' and s[i] < 'X':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)