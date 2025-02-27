def filter_chars(text):
    result = [c for i, c in enumerate(text) if i not in range(19, 34) or c < 'S' or c > '{']
    return ''.join(result)