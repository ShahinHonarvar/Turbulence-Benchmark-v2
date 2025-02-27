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

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        if not str_n:
            break
        if not is_prime(int(str_n)):
            return False
    return True

def get_truncatable_primes_up_to(limit):
    truncatable_primes = []
    for num in range(11, limit + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 80:
        return []
    x = numbers[79]
    result = get_truncatable_primes_up_to(x)
    return sorted(result, reverse=True)