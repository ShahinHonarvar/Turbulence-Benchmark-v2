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

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 33:
        return []
    x = numbers[33]
    right_truncatable_primes = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:i])):
                is_truncatable = False
                break
        if is_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)