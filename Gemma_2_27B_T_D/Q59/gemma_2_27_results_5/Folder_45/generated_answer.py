def all_left_truncatable_prime(nums):
    x = nums[61]
    primes = []
    for num in range(2, x):
        is_prime = True
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True