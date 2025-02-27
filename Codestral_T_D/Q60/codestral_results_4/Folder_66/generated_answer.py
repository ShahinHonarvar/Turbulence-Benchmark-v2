def all_left_right_truncatable_prime(nums):
    x = nums[25]

    def is_truncatable_prime(num):
        if num < 2 or '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if int(str(num)[i:]) not in primes or int(str(num)[:-i]) not in primes:
                return False
        return True
    primes = set()
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    return sorted(filter(is_truncatable_prime, primes), reverse=True)