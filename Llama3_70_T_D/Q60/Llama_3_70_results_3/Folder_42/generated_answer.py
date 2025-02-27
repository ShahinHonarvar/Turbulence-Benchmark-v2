def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[64]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' in prime_str:
            continue
        left, right = (1, len(prime_str) - 1)
        while left < right:
            if not is_prime(int(prime_str[left:right + 1])):
                break
            left += 1
            right -= 1
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)