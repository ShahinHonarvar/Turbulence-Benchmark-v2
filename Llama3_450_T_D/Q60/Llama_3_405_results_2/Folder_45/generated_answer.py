def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable_prime = True
        for i in range(len(str_num)):
            trunc_left = int(str_num[i:])
            trunc_right = int(str_num[:len(str_num) - i])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)