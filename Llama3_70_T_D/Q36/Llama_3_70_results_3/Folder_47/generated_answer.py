def filter_chars(s):
    result = []
    chars_to_remove = set()
    for i in range(len(s)):
        if 45 < i < 57:
            if 'F' < s[i] < 'n':
                chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)