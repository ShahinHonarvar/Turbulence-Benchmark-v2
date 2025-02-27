def all_left_right_truncatable_prime(nums):
    x = nums[20]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_truncatable = True
            for i in range(1, len(str_num)):
                if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i]))):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)