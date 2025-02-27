def all_left_truncatable_prime(nums):
    x = nums[8]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        if '0' not in str(i):
            is_truncatable = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)