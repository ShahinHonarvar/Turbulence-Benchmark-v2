from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    left_truncatable_primes = []
    for i in range(1, x):
        if isprime(i) and str(i)[0] != '0':
            is_left_truncatable_prime = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)