def return_n_smallest_chars(input_string):
    result = {char: ord(char) for char in input_string}
    return sorted(result.items(), key=lambda item: item[1])[:35]