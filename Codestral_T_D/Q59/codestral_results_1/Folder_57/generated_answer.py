def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[54]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        is_left_truncatable_prime = True
        while truncated_num:
            if not is_prime(int(truncated_num)):
                is_left_truncatable_prime = False
                break
            truncated_num = truncated_num[1:]
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes