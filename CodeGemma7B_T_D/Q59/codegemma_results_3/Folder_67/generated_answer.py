from sympy import isprime

def all_left_truncatable_prime(tup):
    for i in range(2, tup[71]):
        if isprime(i) and '0' not in str(i):
            nums = list(str(i))
            if all((isprime(int(''.join(nums[j:]))) for j in range(len(nums)))):
                ans.append(i)
    ans.sort(reverse=True)
    return ans