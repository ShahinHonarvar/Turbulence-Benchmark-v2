from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    result = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        is_ltrunc_prime = True
        while num > 0:
            if not isprime(num):
                is_ltrunc_prime = False
                break
            num = num // 10
        num = num * 10
        while num < x and is_ltrunc_prime:
            if not isprime(num):
                is_ltrunc_prime = False
                break
            num = num // 10 + 10
        if is_ltrunc_prime:
            result.append(num // 10)
    return sorted(list(set(result)))