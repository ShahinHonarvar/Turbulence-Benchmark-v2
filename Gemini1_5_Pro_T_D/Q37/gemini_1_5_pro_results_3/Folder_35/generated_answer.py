def filter_chars(s):
    filtered_chars = set()
    for i in range(155, 404):
        if i < len(s) and '(' <= s[i] <= ']':
            filtered_chars.add(s[i])
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)