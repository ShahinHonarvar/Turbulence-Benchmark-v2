def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[645]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        left_truncatable = True
        right_truncatable = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            left_num = int(str_num[i:])
            right_num = int(str_num[:-i])
            if not is_prime(left_num) or not is_prime(right_num):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes