from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and isprime(i):
            is_left_truncatable = True
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)