def filter_chars(s):
    filtered_chars = set()
    for i in range(20, 80):
        if i < len(s) and '!' <= s[i] <= 'T':
            filtered_chars.add(s[i])
    result = []
    for c in s:
        if c not in filtered_chars:
            result.append(c)
    return ''.join(result)