def all_left_truncatable_prime(nums):
    x = nums[36]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [2]
    for num in range(3, x, 2):
        if is_prime(num):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        is_left_truncatable = True
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)