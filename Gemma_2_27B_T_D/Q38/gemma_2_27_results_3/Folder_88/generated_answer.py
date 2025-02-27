def find_subset_of_length_n(s):
    n = len(s)
    if n < 46:
        return 0
    return factorial(n) // (factorial(46) * factorial(n - 46))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)