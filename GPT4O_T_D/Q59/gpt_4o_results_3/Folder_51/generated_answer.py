def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if '0' in str(n):
        return False
    num_str = str(n)
    while num_str:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    left_trunc_primes = []
    for num in range(2, x):
        if left_truncatable_prime(num):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes)