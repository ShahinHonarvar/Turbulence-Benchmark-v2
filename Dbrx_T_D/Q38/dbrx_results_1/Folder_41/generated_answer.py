def find_subset_of_length_n(elements_set):
    if len(elements_set) < 84:
        return 0
    return int(factorial(len(elements_set)) / (factorial(84) * factorial(len(elements_set) - 84)))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)