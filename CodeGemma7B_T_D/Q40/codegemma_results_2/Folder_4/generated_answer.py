def return_n_smallest_chars(str):
    ascii_values = [(ord(char), char) for char in str]
    ascii_values.sort(reverse=True)
    return [char for _, char in ascii_values[:90]]