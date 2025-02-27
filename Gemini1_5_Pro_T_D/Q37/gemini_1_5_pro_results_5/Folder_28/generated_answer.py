def filter_chars(text):
    filtered_chars = set()
    for i in range(20, 80):
        if i < len(text) and '!' <= text[i] <= 'T':
            filtered_chars.add(text[i])
    result = []
    for char in text:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)