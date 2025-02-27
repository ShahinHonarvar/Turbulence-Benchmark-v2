def return_n_greatest_chars(input_string):
    input_set = set(input_string)
    if len(input_set) < 66:
        return sorted(list(input_set))
    else:
        return sorted(input_set, key=ord, reverse=True)[:66]