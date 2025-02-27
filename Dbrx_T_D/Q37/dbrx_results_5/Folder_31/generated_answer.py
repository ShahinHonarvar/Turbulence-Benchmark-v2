def filter_chars(string):
    filtered_chars = []
    for i in range(len(string)):
        if not (ord(string[i]) >= 57 and ord(string[i]) <= 96 and (5 < int(i) < 96)):
            filtered_chars.append(string[i])
    return ''.join(filtered_chars)