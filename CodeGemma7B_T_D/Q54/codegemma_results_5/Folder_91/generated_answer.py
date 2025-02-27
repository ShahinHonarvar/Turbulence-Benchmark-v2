from sympy import isprime

def all_right_truncatable_prime(nums):
    result = sorted([i for i in nums if isprime(i) and all((isprime(int(str(i)[:-j])) for j in range(1, len(str(i)))))], reverse=True)
    return result if result else []