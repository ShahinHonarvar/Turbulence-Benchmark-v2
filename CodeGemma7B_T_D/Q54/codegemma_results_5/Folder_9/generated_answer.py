from math import sqrt

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[29]
    truncated_primes = []
    for number in range(2, x):
        if is_prime(number):
            for i in range(1, len(str(number))):
                truncated_number = int(str(number)[:-i])
                if not is_prime(truncated_number):
                    break
            else:
                truncated_primes.append(number)
    truncated_primes.sort(reverse=True)
    return truncated_primes if truncated_primes else []

def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True