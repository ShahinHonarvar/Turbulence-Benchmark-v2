def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[87]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num)):
        left = int(str_num[i:])
        right = int(str_num[:len(str_num) - i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True