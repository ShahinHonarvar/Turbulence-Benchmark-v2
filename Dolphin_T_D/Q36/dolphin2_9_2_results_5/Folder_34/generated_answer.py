def filter_chars(string):
    string = list(string)
    for i in range(10, 79):
        if string[i] > '?' and string[i] < 'm':
            string = [char for char in string if char != string[i]]
    return ''.join(string)