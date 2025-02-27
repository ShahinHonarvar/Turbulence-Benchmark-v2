def all_left_truncatable_prime(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[84]
    primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)