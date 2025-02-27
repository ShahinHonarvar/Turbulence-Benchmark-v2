def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num) or not is_prime(num):
            return False
        while num > 0:
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0
            if num > 0 and (not is_prime(num)):
                return False
        return True
    x = nums[97]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)