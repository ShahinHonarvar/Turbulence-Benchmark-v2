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

def is_left_truncatable(prime):
    str_prime = str(prime)
    if '0' in str_prime:
        return False
    for i in range(len(str_prime)):
        if not is_prime(int(str_prime[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)