def filter_chars(s):
    filtered_chars = list(s)
    for i in range(58, 69):
        if i < len(s) and '(' < s[i] < 'W':
            char = s[i]
            filtered_chars = [x for x in filtered_chars if x != char]
    return ''.join(filtered_chars)