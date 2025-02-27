from sympy import isprime

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for num in range(1, x):
        str_num = str(num)
        if isprime(num) and all((isprime(int(str_num[:i])) for i in range(len(str_num) - 1, -1, -1))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)