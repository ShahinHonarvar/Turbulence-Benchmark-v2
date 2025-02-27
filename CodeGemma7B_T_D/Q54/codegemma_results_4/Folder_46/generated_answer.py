def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[33]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_prime(number):
            for i in range(1, len(str(number))):
                if not is_prime(int(str(number)[:-i])):
                    break
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True