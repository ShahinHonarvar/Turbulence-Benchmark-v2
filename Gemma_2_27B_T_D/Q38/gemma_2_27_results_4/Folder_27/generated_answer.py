def find_subset_of_length_n(elements):
    n = len(elements)
    return int(factorial(n) / (factorial(56) * factorial(n - 56)))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)