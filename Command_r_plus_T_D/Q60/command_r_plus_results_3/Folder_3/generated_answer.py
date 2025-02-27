def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    left_right_primes = []
    for num in nums:
        if num < 10:
            continue
        str_num = str(num)
        left_truncatable = all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1)))
        right_truncatable = all((is_prime(int(str_num[i:])) for i in range(len(str_num) - 1, -1, -1)))
        if left_truncatable and right_truncatable:
            left_right_primes.append(num)
    return sorted(left_right_primes)