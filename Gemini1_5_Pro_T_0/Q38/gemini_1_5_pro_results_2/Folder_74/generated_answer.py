def find_subset_of_length_n(set_of_elements):
    n = 48
    number_of_elements = len(set_of_elements)
    if number_of_elements < n:
        return 0
    if number_of_elements == n:
        return 1
    return math.factorial(number_of_elements) // (math.factorial(n) * math.factorial(number_of_elements - n))