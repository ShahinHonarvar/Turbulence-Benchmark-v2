from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if n % 10 != 0 else n // 10
            if not isprime(n):
                return False
        return True
    x = numbers[71]
    return sorted([num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)], reverse=True) or []