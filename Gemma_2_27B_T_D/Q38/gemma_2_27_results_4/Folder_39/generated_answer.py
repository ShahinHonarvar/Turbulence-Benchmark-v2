def find_subset_of_length_n(elements):
    n = len(elements)
    if 59 > n:
        return 0
    return factorial(n) // (factorial(59) * factorial(n - 59))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)