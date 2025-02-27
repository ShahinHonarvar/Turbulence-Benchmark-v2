def filter_chars(s):
    filtered_chars = set()
    for i in range(15, 56):
        if i < len(s) and 'W' <= s[i] <= '{':
            filtered_chars.add(s[i])
    result = []
    for c in s:
        if c not in filtered_chars:
            result.append(c)
    return ''.join(result)