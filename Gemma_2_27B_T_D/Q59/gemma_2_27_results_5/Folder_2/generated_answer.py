def all_left_truncatable_prime(nums):
    x = nums[618]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            tmp = str(i)
            flag = True
            for j in range(1, len(tmp)):
                if not is_prime(int(tmp[j:])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes)