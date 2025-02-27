def return_n_greatest_chars(input_str):
    return sorted([char for char in input_str if input_str.count(char) == 1], key=lambda x: ord(x), reverse=True)[:47]