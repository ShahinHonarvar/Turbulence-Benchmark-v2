def all_left_right_truncatable_prime(nums):
    x = nums[55]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' not in prime_str:
            is_truncatable = True
            left, right = (prime_str[1:], prime_str[:-1])
            while len(left) > 1 and len(right) > 1:
                if not (is_prime(int(left)) and is_prime(int(right))):
                    is_truncatable = False
                    break
                left, right = (left[1:], right[:-1])
            if is_truncatable:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True