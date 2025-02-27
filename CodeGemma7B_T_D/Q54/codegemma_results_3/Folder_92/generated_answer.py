from sympy import isprime

def all_right_truncatable_prime(nums):
    ans = []
    x = nums[7]
    for i in range(2, x):
        if isprime(i):
            temp = i - i % 10
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                ans.append(i)
    return sorted(ans)