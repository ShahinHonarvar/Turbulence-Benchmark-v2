def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable(prime):
    str_prime = str(prime)
    for i in range(len(str_prime)):
        if not is_prime(int(str_prime[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = []
    for n in range(2, x):
        if '0' not in str(n) and is_prime(n) and is_left_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)