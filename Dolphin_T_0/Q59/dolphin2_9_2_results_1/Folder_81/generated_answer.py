import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(tuple_of_pos_integers):
    x = tuple_of_pos_integers[98]
    prime_numbers = []
    for n in range(2, x):
        if all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))):
            prime_numbers.append(n)
    return sorted(prime_numbers)