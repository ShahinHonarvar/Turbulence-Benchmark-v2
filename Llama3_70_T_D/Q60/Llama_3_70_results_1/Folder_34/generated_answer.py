def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = nums[18]
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    left_right_truncatable_primes = []
    for prime in truncatable_primes:
        prime_str = str(prime)
        while len(prime_str) > 2:
            prime_str = prime_str[1:-1]
            if not is_prime(int(prime_str)):
                break
        else:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)