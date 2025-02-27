from sympy import isprime

def composite_nums_between_indices(data):
    return {num for num in data[12:93] if isprime(num) == False}