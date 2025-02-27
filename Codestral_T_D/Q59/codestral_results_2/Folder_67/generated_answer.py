def all_left_truncatable_prime(nums):
    x = nums[71]
    truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        if num < 10:
            return True
        return is_left_truncatable_prime(int(str(num)[1:]))
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes