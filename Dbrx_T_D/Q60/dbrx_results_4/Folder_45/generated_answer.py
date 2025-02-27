from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    result = []

    def is_left_right_truncatable(n):
        if not isprime(n):
            return False
        while n > 0:
            if '0' in str(n) or not isprime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)