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

def is_left_truncatable(n):
    if '0' in str(n):
        return False
    num = str(n)
    while num:
        if not is_prime(int(num)):
            return False
        num = num[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    truncatable_primes = [n for n in range(2, x) if is_left_truncatable(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes