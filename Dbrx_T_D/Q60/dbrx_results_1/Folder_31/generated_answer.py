from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[50]
    lr_primes = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            l_num, r_num = (int(str(num)[0]), int(str(num)[-1]))
            if isprime(l_num) and isprime(r_num):
                lr_primes.append(num)
    return sorted(lr_primes, reverse=True)