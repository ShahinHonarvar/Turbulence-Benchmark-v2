from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[22]
    result = []
    for i in range(2, x):
        if isprime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not isprime(int(str_i[:-j])):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)