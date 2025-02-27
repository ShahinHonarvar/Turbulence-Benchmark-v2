def find_subset_of_length_n(input_set):
    if len(input_set) < 29:
        return 0
    return int(factorial(len(input_set)) / (factorial(29) * factorial(len(input_set) - 29)))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)