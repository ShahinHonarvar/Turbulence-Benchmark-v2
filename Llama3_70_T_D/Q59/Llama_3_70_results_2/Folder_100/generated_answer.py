def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(nums):
    x = nums[26]
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                break
        else:
            truncatable_primes.append(prime)
    return truncatable_primes