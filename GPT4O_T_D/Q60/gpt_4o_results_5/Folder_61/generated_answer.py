def all_left_right_truncatable_prime(nums):
    if len(nums) <= 3:
        return []
    x = nums[3]

    def is_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:len(s) - i]))):
                return False
        return True
    truncated_primes = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            truncated_primes.append(i)
    return sorted(truncated_primes, reverse=True)