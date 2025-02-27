def is_prime(n):
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = [i for i in range(2, x) if is_prime(i)]
    trunc_primes = [i for i in primes if all((is_prime(int(str(i)[1:])) for j in range(1, len(str(i)))))]
    return sorted(trunc_primes, reverse=True)