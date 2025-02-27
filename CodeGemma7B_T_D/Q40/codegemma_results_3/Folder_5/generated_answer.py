def return_n_smallest_chars(str):
    list_of_tuples = sorted(enumerate(str), key=lambda x: x[1])
    return [i[1] for i in list_of_tuples[:46]][::-1]