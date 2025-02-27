from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[35]
    right_trunc_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            if all((isprime(int(str_num[:i])) for i in range(1, len(str_num)))):
                right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)