def all_left_right_truncatable_prime(nums):
    x = nums[70]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str), 1, -1):
            if not is_prime(int(num_str[:i])) or not is_prime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)