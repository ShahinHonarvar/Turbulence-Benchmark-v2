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
    x = numbers[7]
    truncatable_primes = set()
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_right_truncatable = True
        for i in range(len(str_num)):
            left_trunc = str_num[i:]
            right_trunc = str_num[:-i or None]
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))