def all_left_truncatable_prime(nums):
    x = nums[14]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        str_i = str(i)
        if '0' not in str_i:
            is_truncatable = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)