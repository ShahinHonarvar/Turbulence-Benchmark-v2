def all_left_right_truncatable_prime(nums):
    x = nums[758]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            n = num
            while n > 9:
                n //= 10
                if not is_prime(n):
                    is_truncatable = False
                    break
            n = num
            while n > 9:
                n %= 10 ** (len(str(n)) - 1)
                if not is_prime(n):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                primes.append(num)
    return sorted(primes)