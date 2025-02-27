def all_left_truncatable_prime(nums):
    x = nums[88]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        i = str(i)
        if '0' not in i:
            is_truncatable = True
            for j in range(len(i)):
                if not is_prime(int(i[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(int(i))
    return primes