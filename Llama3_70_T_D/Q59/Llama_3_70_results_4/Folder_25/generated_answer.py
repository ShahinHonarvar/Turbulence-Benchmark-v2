def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[92]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        is_left_truncatable_prime = True
        while len(truncated_num) > 1:
            if not is_prime(int(truncated_num)):
                is_left_truncatable_prime = False
                break
            truncated_num = truncated_num[1:]
        if is_left_truncatable_prime and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)