from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[73]
    lst = []
    for i in range(1, x):
        if isprime(i) and (not i < 10) and (str(i)[0] != '0'):
            is_left_truncatable = True
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                lst.append(i)
    return sorted(lst, reverse=True)