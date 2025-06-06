def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[100]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)