from sympy import isprime

def all_left_truncatable_prime(tp):
    nums = set(range(9, tp[29]))
    for prime in nums:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        for i in range(1, len(str_prime)):
            if not isprime(int(str_prime[i:])):
                nums.remove(prime)
                break
    return sorted(nums, reverse=True)