def filter_chars(data):
    for i in range(0, 4):
        data = data.replace(data[i], '')
    return data