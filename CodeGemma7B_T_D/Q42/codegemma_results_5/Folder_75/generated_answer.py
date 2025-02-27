from math import sqrt
        from functools import reduce

def prime_factors(lst):
    s = set()
    number = lst[80]
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            s.add(i)
            number //= i
    if number > 1:
        s.add(number)
    return s