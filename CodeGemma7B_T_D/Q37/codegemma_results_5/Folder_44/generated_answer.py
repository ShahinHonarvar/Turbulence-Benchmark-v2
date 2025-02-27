def filter_chars(string):
    for i in range(21, 44):
        if string[i] >= '+' and string[i] <= '8':
            string = string[:i] + string[i + 1:]
    return string