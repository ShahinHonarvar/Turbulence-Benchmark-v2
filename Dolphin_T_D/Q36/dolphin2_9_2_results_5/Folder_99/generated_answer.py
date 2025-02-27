def filter_chars(string):
    string_list = list(string)
    for i in range(476, 948):
        if string[i] > 'b' and string[i] < 'd':
            string_list = [char for char in string_list if char != string[i]]
    return ''.join(string_list)