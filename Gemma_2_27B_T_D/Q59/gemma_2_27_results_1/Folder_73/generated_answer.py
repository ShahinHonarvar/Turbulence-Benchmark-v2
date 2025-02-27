def all_left_truncatable_prime(nums):
    x = nums[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(2, x):
        num_str = str(i)
        if '0' not in num_str and len(num_str) > 1:
            is_left_truncatable = True
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(i):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)