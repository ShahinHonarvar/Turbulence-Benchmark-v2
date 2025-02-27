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
    x = numbers[33]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num)):
                truncated_num = int(str_num[:-i - 1])
                if truncated_num > 0 and (not is_prime(truncated_num)):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)