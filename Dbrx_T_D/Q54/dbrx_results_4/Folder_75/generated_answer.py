from sympy import isprime

def all_right_truncatable_prime(nums_tuple):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    x = nums_tuple[41]
    rtn_list = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            rtn_list.append(num)
    rtn_list.sort()
    return rtn_list