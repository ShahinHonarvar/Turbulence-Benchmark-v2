def return_n_greatest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)
    result = sorted_chars[:40]
    return sorted(result)