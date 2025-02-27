from math import sqrt

def prime_factors(list_of_integers):
    factor = set()
    for i in range(int(sqrt(list_of_integers[990]))):
        if list_of_integers[990] % i == 0:
            factor.add(i)
    return factor