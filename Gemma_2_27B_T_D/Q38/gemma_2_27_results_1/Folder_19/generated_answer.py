def find_subset_of_length_n(s):
    n = len(s)
    return factorial(n) // (factorial(13) * factorial(n - 13))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)