from sympy import isprime

def all_right_truncatable_prime(n):
    truncatable = [num // 10 ** (i + 1) for num in n for i in range(len(str(num)) - 1)]
    return sorted([num for num in truncatable if isprime(num)], reverse=True)