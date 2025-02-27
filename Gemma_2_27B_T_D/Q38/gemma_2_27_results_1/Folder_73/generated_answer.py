def find_subset_of_length_n(s):
    n = len(s)
    if n < 41:
        return 0
    return factorial(n) / (factorial(41) * factorial(n - 41))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)