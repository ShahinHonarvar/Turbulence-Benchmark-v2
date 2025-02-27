from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[26]
    left_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            is_left_truncatable_prime = True
            for digit in str(num):
                if not isprime(int(str(num)[i:])):
                    is_left_truncatable_prime = False
                    break
                num = int(str(num)[1:])
            if is_left_truncatable_prime:
                left_truncatable_primes.append(num)
    return sorted(list(set(left_truncatable_primes)))