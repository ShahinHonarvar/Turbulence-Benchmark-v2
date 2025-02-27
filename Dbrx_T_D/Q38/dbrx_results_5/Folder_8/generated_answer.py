def find_subset_of_length_n(input_set):
    if not isinstance(input_set, set) or len(input_set) < 49:
        return 0
    return int(factorial(len(input_set)) / (factorial(49) * factorial(len(input_set) - 49)))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)