def all_left_right_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            if check_truncatable(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def check_truncatable(num):
    str_num = str(num)
    if len(str_num) < 3:
        return True
    for i in range(len(str_num)):
        for j in range(i + 2, len(str_num) + 1):
            substr = int(str_num[i:j])
            if is_prime(substr):
                continue
            else:
                return False
    return True