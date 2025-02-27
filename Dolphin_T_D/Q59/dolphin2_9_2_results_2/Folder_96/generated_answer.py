def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(tuple_numbers):
    x = tuple_numbers[2]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            if str(i).count('0') == 0:
                truncated = i
                while truncated > 0:
                    if not is_prime(truncated):
                        break
                    truncated = int(str(truncated)[1:])
                else:
                    primes.append(i)
    primes.sort()
    return primes