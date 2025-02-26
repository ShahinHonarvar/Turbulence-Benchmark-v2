def filter_chars(string):
    result = []
    to_remove = set()
    for i in range(32, 70):
        if i < len(string) and 'B' < string[i] < 'v':
            to_remove.add(string[i])
    for char in string:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)