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

def truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    trunc = n
    while trunc > 9:
        trunc = int(str(trunc)[1:])
        if not is_prime(trunc):
            return False
    trunc = n
    while trunc > 9:
        trunc = int(str(trunc)[:-1])
        if not is_prime(trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)