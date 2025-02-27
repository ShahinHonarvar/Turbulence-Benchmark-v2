from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        num_str = str(n)
        while num_str:
            if not isprime(int(num_str)) or '0' in num_str:
                return False
            num_str = num_str[1:]
        return True
    x = numbers[49]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])