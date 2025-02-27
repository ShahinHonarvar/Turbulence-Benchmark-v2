from sympy import isprime

def all_right_truncatable_prime(nums):
    if len(nums) <= 803:
        return []
    x = nums[803]

    def is_right_truncatable_prime(num):
        if not isprime(num):
            return False
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not isprime(int(str_num)):
                return False
        return True
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return result