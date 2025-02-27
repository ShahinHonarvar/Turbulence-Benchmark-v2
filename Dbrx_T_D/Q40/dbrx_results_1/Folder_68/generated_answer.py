def return_n_smallest_chars(input_string):
    distinct_chars = list(set(input_string))
    distinct_chars.sort(key=lambda x: ord(x))
    return distinct_chars[:89][::-1]