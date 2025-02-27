def find_subset_of_length_n(elements):
    if len(elements) < 20:
        return 0
    elif len(elements) == 20:
        return 1
    else:
        return (1 << len(elements) - 20) * (factorial(len(elements)) // (factorial(len(elements) - 20) * factorial(20)))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)