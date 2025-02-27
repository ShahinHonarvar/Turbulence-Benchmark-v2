from sympy import isprime

def all_left_right_truncatable_prime(upper_limit_tuple):
    x = upper_limit_tuple[29]
    ltrp_list = []

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n //= 10
            if not isprime(n):
                return False
        return True
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            ltrp_list.append(num)
    ltrp_list.sort(reverse=True)
    return ltrp_list