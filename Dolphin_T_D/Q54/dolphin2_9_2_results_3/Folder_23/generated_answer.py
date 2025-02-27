import sympy

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[77]
    right_truncatable_primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            trunc = num
            while trunc > 0:
                if not sympy.isprime(int(str(trunc)[::-1])):
                    break
                trunc = trunc // 10
                if trunc == 1:
                    right_truncatable_primes.append(num)
                    break
    return sorted(right_truncatable_primes, reverse=True)