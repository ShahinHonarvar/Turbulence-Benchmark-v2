def all_left_right_truncatable_prime(nums):
    x = nums[49]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable = True
        while len(num_str) > 1:
            if not is_prime(int(num_str)) or not is_prime(int(num_str[::-1])):
                is_truncatable = False
                break
            num_str = num_str[1:-1]
        if is_truncatable:
            primes.append(num)
    return sorted(primes)