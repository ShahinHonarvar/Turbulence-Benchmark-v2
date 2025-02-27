def all_left_right_truncatable_prime(nums):
    x = nums[73]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x, 1, -1):
        num_str = str(i)
        if '0' in num_str:
            continue
        is_truncatable = True
        temp = i
        while temp > 9:
            temp = int(str(temp)[1:])
            if not is_prime(temp):
                is_truncatable = False
                break
        temp = i
        while temp > 9:
            temp = int(str(temp)[:-1])
            if not is_prime(temp):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)