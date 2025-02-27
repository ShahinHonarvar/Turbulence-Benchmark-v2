def filter_chars(str):
    characters = list(str)
    filtered_chars = []
    for i in range(15, 85):
        if characters[i] > 'I' and characters[i] < 'M':
            filtered_chars.append(characters[i])
    return ''.join(filtered_chars)