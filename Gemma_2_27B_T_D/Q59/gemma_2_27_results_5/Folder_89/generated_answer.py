def all_left_truncatable_prime(nums):
    x = nums[97]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' not in num_str and is_prime(num):
            is_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)