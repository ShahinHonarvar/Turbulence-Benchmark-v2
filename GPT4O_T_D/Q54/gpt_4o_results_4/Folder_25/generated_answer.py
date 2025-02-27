from sympy import isprime

def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True
    x = nums[92]
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(result)