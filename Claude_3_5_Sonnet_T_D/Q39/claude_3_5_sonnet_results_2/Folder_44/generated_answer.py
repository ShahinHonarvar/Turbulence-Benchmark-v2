def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)
    result = sorted_chars[:73] if len(sorted_chars) >= 73 else sorted_chars + [chr(0)] * (73 - len(sorted_chars))
    return sorted(result)