def all_left_right_truncatable_prime(nums):
    x = nums[28]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            while len(str(num)) > 1:
                num = int(str(num)[1:])
                if not is_prime(num):
                    is_truncatable = False
                    break
            num = int(str(num)[:-1])
            while len(str(num)) > 1:
                num = int(str(num)[:-1])
                if not is_prime(num):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)