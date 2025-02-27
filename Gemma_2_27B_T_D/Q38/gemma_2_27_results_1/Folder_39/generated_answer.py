def find_subset_of_length_n(elements):
    n = len(elements)
    return factorial(n) // (factorial(59) * factorial(n - 59))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)