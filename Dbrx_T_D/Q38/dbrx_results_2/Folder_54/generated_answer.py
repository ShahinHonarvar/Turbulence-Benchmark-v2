def find_subset_of_length_n(elements_set):
    if len(elements_set) < 51:
        return 0
    elif len(elements_set) == 51:
        return 1
    else:
        return (1 << len(elements_set) - 51) * (factorial(51) * factorial(len(elements_set) - 51))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)