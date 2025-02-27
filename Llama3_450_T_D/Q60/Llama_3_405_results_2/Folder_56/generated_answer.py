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
    x = numbers[30]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable = True
        for i in range(1, len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
            truncated_num = int(num_str[:-i])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes