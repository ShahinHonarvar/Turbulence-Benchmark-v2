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

def is_right_truncatable_prime(num):
    str_num = str(num)
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[:-1]
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 11:
        return []
    x = numbers[10]
    right_truncatable_primes = [num for num in range(x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes, reverse=True)