from sympy import isprime

def composite_nums_between_indices(lst):
    result = set()
    for i in range(21, 98):
        if not isprime(lst[i]):
            result.add(lst[i])
    return result