def all_left_right_truncatable_prime(nums):
    x = nums[630]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' not in str(i):
            is_truncatable = True
            num_str = str(i)
            while len(num_str) > 1:
                if not (is_prime(int(num_str)) and is_prime(int(num_str[:-1]))):
                    is_truncatable = False
                    break
                num_str = num_str[1:-1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)