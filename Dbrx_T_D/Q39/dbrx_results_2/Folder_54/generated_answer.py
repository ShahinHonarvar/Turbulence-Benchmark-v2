def return_n_greatest_chars(input_string):
    distinct_chars = list(set(input_string))
    distinct_chars.sort(reverse=True)
    return distinct_chars[:79]