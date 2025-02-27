def all_right_truncatable_prime(nums):
    x = nums[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            flag = True
            for j in range(len(s) - 1, 0, -1):
                if not is_prime(int(s[:j])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes, reverse=True)