def return_n_smallest_chars(string):
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    ascii_values.sort(reverse=True)
    return [chr(value) for value in ascii_values[:37]]