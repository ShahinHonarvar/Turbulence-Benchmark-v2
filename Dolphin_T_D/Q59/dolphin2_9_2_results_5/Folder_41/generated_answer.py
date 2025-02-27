import sympy

def all_left_truncatable_prime(x):
    left_truncatable_prime = []
    for num in range(x, 0, -1):
        if sympy.isprime(num):
            n = num
            while n != 0:
                if not sympy.isprime(n):
                    break
                n = n // 10
                if n == 0:
                    left_truncatable_prime.append(num)
    return left_truncatable_prime