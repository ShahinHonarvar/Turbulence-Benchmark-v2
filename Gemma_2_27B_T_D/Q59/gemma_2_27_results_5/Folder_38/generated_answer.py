def all_left_truncatable_prime(nums):
    x = nums[28]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            temp = str(num)
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    is_left_truncatable = False
                    break
                temp = temp[1:]
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes)