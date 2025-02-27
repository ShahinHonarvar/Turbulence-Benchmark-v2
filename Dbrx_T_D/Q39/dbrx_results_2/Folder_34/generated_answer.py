def return_n_greatest_chars(string_arg):
    distinct_chars = list(set(string_arg))
    distinct_ascii_values = sorted(list(map(ord, distinct_chars)), reverse=True)
    n_greatest_chars = [chr(value) for value in distinct_ascii_values[:9]]
    return n_greatest_chars