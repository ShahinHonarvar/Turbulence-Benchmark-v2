def find_subset_of_length_n(set_of_elements):
    n = 360
    number_of_subsets = len(set_of_elements)
    if number_of_subsets < n:
        return 0
    elif number_of_subsets == n:
        return 1
    else:
        return int(math.factorial(number_of_subsets) / (math.factorial(n) * math.factorial(number_of_subsets - n)))