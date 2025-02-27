def all_left_right_truncatable_prime(nums):

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

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(len(s)):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:i + 1]))):
                return False
        return True
    if len(nums) < 98:
        return []
    x = nums[97]
    truncatable_primes = [n for n in range(10, x + 1) if is_left_right_truncatable_prime(n)]
    return truncatable_primes