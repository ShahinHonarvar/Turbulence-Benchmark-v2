def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[81]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num) and all((is_prime(int(str_num[i:j])) for i in range(len(str_num)) for j in range(i + 1, len(str_num) + 1) if len(str_num[i:j]) > 1)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)