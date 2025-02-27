def return_n_smallest_chars(input_string):
    chars_and_values = sorted(((c, ord(c)) for c in set(input_string)))
    smallest_values = [value for _, value in chars_and_values[:29]]
    result = [chr(value) for value in smallest_values]
    result.sort(reverse=True)
    return result