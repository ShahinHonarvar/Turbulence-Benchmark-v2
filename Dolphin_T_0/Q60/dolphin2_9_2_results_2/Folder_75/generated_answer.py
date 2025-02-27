def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    sqr = 3
    while sqr * sqr <= n and n % sqr != 0:
        sqr += 2
    return sqr * sqr > n

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
        if len(str_num) == 1 and is_prime(int(str_num)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)