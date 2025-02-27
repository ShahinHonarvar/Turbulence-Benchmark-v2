from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 99:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n % 10 != 0 else int(str(n)[:-1])
        return isprime(n)
    x = nums_tuple[100]
    return sorted([num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)], reverse=True) or []