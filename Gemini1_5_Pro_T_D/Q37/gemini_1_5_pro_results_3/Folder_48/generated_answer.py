def filter_chars(s):
    to_remove = set()
    for i in range(513, 878):
        if i < len(s) and '?' <= s[i] <= 'n':
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)