def find_subset_of_length_n(s):
    n = len(s)
    return factorial(n) // (factorial(32) * factorial(n - 32))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)