def all_left_right_truncatable_prime(nums):
    x = nums[42]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n = str(n)
        while len(n) > 1:
            if not (is_prime(int(n)) and is_prime(int(n[:-1]))):
                return False
            n = n[:-1]
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes