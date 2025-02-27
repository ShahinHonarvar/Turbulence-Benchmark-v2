from sympy import isprime

def all_left_truncatable_prime(nums):
    result = []
    for num in nums:
        if not isprime(num):
            continue
        num_str = str(num)
        if '0' in num_str:
            continue
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)