def all_left_right_truncatable_prime(nums):
    x = nums[77]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        temp = num_str
        while len(temp) > 1:
            if not is_prime(int(temp)):
                is_truncatable = False
                break
            temp = temp[1:]
        temp = num_str
        while len(temp) > 1:
            if not is_prime(int(temp)):
                is_truncatable = False
                break
            temp = temp[:-1]
        if is_truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)