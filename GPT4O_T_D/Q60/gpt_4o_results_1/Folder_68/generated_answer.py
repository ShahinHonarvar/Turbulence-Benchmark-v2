def all_left_right_truncatable_prime(nums):
    x = nums[1]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        s = str(n)
        for length in range(1, len(s)):
            left_truncate = int(s[length:])
            right_truncate = int(s[:-length])
            if not (is_prime(left_truncate) and is_prime(right_truncate)):
                return False
        return True
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)