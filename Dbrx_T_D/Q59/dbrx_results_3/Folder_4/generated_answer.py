from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[95]
    left_truncatable_primes = []
    for number in range(1, x):
        is_left_truncatable_prime = True
        for digit in str(number):
            if digit == '0' or not isprime(int(digit)):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            for i in range(1, len(str(number))):
                if not isprime(int(str(number)[i:])):
                    is_left_truncatable_prime = False
                    break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)