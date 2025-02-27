def return_n_greatest_chars(input_string):
    sorted_string = sorted(input_string, key=lambda x: ord(x), reverse=True)
    return sorted(sorted_string[:35])