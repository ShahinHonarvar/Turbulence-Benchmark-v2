def filter_chars(chunk):
    for i in range(323, 526):
        if chunk[i] > '(':
            if chunk[i] < 'O':
                chunk = chunk[:i] + chunk[i + 1:]
    return chunk