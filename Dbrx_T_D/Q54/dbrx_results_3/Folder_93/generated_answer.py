from sympy import isprime

def all_right_truncatable_prime(x):

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    result = []
    for num in range(1, x):
        if isprime(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result)