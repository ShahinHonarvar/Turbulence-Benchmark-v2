def filter_chars(s):
    filtered_chars = list(s)
    for i in range(56, 84):
        if ';' < filtered_chars[i] < 'z':
            filtered_chars = [char for char in filtered_chars if char != filtered_chars[i]]
    return ''.join(filtered_chars)