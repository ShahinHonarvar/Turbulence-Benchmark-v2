def remove_repeat_chars(test_string):
    string_list = list(test_string)
    for i in range(44, 78):
        if string_list[i] in string_list[i + 1:77]:
            string_list[i:i + string_list[i + 1:77].count(string_list[i]) + 1] = []
    return ''.join(string_list)