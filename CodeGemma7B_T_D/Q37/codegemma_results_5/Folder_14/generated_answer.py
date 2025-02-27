def filter_chars(str):
    filtered_str = []
    for i, char in enumerate(str):
        if i >= 35 and i <= 98 and (char >= 'A') and (char <= 'b'):
            continue
        filtered_str.append(char)
    return ''.join(filtered_str)