def find_subset_of_length_n(s):
    n = len(s)
    return factorial(n) // (factorial(312) * factorial(n - 312))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)