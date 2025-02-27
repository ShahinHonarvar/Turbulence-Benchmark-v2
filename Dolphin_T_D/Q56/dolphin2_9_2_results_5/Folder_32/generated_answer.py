def all_substring_of_size_n(input_string):
    length = len(input_string)
    return list(set([input_string[i:i + 71] for i in range(length - 70)]))