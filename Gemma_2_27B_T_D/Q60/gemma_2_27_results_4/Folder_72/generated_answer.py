from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[31]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' not in s and isprime(i):
            is_truncatable = True
            for j in range(1, len(s)):
                if not (isprime(int(s[j:])) and isprime(int(s[:-j]))):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)