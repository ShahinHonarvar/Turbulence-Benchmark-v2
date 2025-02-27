def filter_chars(string):
    filtered = []
    for i in range(31, 70):
        if string[i] > 'B' and string[i] < 'v':
            continue
        filtered.append(string[i])
    return ''.join(filtered)