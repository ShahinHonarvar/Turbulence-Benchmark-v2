from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[70]
    rtp_primes = []
    for num in range(x - 1, 1, -1):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            rtp_primes.append(num)
    return sorted(rtp_primes, reverse=True)