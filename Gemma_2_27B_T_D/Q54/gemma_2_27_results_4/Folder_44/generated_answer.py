def all_right_truncatable_prime(nums):
    x = nums[39]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        s = str(i)
        flag = True
        for j in range(len(s), 0, -1):
            if not is_prime(int(s[:j])):
                flag = False
                break
        if flag:
            primes.append(i)
    return sorted(primes)