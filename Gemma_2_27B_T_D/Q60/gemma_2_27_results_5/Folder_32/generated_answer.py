def all_left_right_truncatable_prime(nums):
    x = nums[42]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        n = str(i)
        if '0' not in n:
            is_truncatable = True
            while len(n) > 1:
                if not is_prime(int(n)) or not is_prime(int(n[1:])):
                    is_truncatable = False
                    break
                n = n[1:-1]
            if is_truncatable and is_prime(i):
                primes.append(i)
    return sorted(primes)