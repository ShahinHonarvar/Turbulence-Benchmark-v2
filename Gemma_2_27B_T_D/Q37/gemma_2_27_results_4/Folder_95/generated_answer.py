def filter_chars(s):
    result = []
    removed_chars = set()
    for i, char in enumerate(s):
        if 35 <= i <= 40 and '(' <= char <= 'l':
            removed_chars.add(char)
        elif char not in removed_chars:
            result.append(char)
    return ''.join(result)