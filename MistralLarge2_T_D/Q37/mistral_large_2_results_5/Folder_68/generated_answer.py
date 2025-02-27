def filter_chars(s):
    filtered_chars = []
    for i in range(7, 10):
        if '6' <= s[i] <= 'w':
            filtered_chars.append(s[i])
    return ''.join([char for char in s if char not in filtered_chars])