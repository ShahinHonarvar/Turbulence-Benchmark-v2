from sympy import isprime

def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = nums[85]
    result = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)