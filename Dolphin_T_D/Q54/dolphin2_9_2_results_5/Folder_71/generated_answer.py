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

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = []
    i = 9
    while i < x:
        if is_prime(i) and is_prime(int(str(i)[1:])):
            primes.append(i)
            i += 1
        else:
            i += 1
    return sorted(primes, reverse=True)