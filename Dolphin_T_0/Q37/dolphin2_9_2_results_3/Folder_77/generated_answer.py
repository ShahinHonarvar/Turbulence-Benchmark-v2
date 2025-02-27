def filter_chars(string_input):
    for x in range(384, 412):
        if string_input[x] >= '/' and string_input[x] <= '8':
            string_input = string_input.replace(string_input[x], '')
    return string_input