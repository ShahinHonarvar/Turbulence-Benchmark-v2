def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[18]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            trunc_prime = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                left_trunc = int(str_num[i:])
                right_trunc = int(str_num[:-i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    trunc_prime = False
                    break
            if trunc_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)