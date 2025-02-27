from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[784]
    primes = []
    for i in range(2, x):
        if isprime(i):
            is_left_truncatable = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes)