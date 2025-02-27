from sympy import isprime

def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[38]
    right_truncatable_primes = []
    for num in reversed(range(2, x + 1)):
        if isprime(num):
            truncation_is_prime = True
            for i in range(10 ** (len(str(num)) - 1)):
                if not isprime(int(str(num)[-i - 1:])):
                    truncation_is_prime = False
                    break
            if truncation_is_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)