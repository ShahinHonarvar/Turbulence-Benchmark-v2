def all_left_truncatable_prime(nums):

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
    x = nums[32]
    ltp_primes = []
    for i in range(2, x):
        num_str = str(i)
        if is_prime(i) and '0' not in num_str:
            is_ltp = all((is_prime(int(num_str[j:])) for j in range(1, len(num_str))))
            if is_ltp:
                ltp_primes.append(i)
    return sorted(ltp_primes)