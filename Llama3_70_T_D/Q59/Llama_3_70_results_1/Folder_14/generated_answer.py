def all_left_truncatable_prime(nums):
    x = nums[78]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated = str(num)
        is_truncatable_prime = True
        while len(truncated) > 1:
            truncated = truncated[1:]
            if not is_prime(int(truncated)):
                is_truncatable_prime = False
                break
        if is_prime(num) and is_truncatable_prime:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)