from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[784]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and isprime(num):
            current = num
            while current > 0:
                current = int(str(current)[:-1])
                if not isprime(current):
                    break
                if current == 0:
                    result.append(num)
    return sorted(result)