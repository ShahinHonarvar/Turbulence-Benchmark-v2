def all_right_truncatable_prime(nums):
    x = nums[41]

    def is_prime(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def get_truncatable_primes():
        primes = []
        for num in range(2, x):
            if is_prime(num):
                s = str(num)
                for i in range(1, len(s)):
                    if not is_prime(int(s[:-i])):
                        break
                else:
                    primes.append(num)
        return primes
    return sorted(get_truncatable_primes(), reverse=True)