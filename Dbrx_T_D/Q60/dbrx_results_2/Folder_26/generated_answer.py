from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[81]

    def is_left_right_truncatable_prime(n):
        if not (1 < n < 10 ** 6 and '0' not in str(n)):
            return False
        while n > 9:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
        return True
    result = [num for num in range(10, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(result, reverse=True)