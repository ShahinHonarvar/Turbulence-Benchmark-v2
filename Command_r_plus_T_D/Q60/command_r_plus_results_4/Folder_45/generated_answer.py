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
    if str(n).count('0') > 0:
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[:i + 1])) or not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)