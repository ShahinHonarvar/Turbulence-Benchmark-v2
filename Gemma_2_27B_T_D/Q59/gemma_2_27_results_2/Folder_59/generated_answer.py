def all_left_truncatable_prime(nums):
    x = nums[84]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            flag = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes, reverse=True)