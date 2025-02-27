def filter_chars(input_string):
    start_index = 42
    end_index = 92
    lower_bound = '/'
    upper_bound = 'a'
    result = ''
    for i in range(len(input_string)):
        if input_string[i] < lower_bound or input_string[i] > upper_bound or i < start_index or (i > end_index):
            result += input_string[i]
    return result