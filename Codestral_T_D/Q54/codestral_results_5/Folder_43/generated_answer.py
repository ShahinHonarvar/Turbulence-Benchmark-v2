import sympy

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[89]
    right_truncatable_primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            is_right_truncatable = True
            trunc_num = num
            while trunc_num > 0:
                trunc_num = trunc_num // 10
                if not sympy.isprime(trunc_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)