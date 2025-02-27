def all_right_truncatable_prime(nums):
    x = nums[97]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            i_str = str(i)
            flag = True
            for j in range(len(i_str) - 1, 0, -1):
                if not is_prime(int(i_str[:j])):
                    flag = False
                    break
            if flag:
                primes.append(i)
    return sorted(primes, reverse=True)