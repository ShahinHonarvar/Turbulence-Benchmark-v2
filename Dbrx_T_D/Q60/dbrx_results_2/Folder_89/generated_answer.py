from sympy import isprime

def is_left_right_truncatable_prime(n):
    if n < 10:
        return isprime(n)
    if '0' in str(n):
        return False
    while n % 10 > 1 and n > 9:
        n //= 10
        if not isprime(n):
            return False
    return is_left_right_truncatable_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    return sorted([num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)], reverse=True) or []