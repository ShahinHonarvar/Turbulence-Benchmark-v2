def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(start):
    primes = []
    for num in range(start - 1, 0, -1):
        if is_prime(num):
            is_left_truncatable = True
            for digit in range(1, len(str(num)) + 1):
                if not is_prime(int(str(num)[digit:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return primes