def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[77]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if len(prime_str) > 1 and (int(prime_str[:-1]) in primes or int(prime_str[1:]) in primes):
            truncatable = True
            for i in range(1, len(prime_str) - 1):
                if int(prime_str[i:-i]) not in primes:
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)