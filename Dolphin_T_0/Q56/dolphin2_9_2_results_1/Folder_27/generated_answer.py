def all_substring_of_size_n(input_string):
    res = set()
    for i in range(len(input_string)):
        if len(input_string[i:i + 57]) == 57:
            if len(set(input_string[i:i + 57])) == 57:
                res.add(input_string[i:i + 57])
    return list(res)