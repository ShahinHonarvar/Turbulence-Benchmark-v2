def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[65]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if '0' not in str(prime):
            str_prime = str(prime)
            if all((is_prime(int(str_prime[i:len(str_prime) - j])) for i in range(len(str_prime)) for j in range(len(str_prime)) if i + j < len(str_prime))):
                truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)