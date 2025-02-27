def filter_chars(string):
    filtered = ''
    for i in range(len(string)):
        if string[i] != string[i + 58] and string[i] != string[i + 81]:
            filtered += string[i]
    return filtered