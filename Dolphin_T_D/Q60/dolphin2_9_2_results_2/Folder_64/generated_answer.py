def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num = str(num)
        if '0' in num:
            return False
        while len(num) > 1:
            if not is_prime(int(num)):
                return False
            num = num[1:-1]
        return is_prime(int(num))
    primes = []
    for num in nums:
        if is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)