from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[79]
    primes = []
    for n in range(2, x):
        if '0' in str(n):
            continue
        if isprime(n):
            is_left_truncatable = True
            trunc_num = str(n)
            while len(trunc_num) > 1:
                trunc_num = trunc_num[1:]
                if not isprime(int(trunc_num)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(n)
    return sorted(primes, reverse=True)