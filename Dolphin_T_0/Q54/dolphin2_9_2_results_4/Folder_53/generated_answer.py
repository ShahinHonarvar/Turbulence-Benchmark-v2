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
    x = numbers[86]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatables = []
    for prime in primes:
        copy = prime
        while copy > 1:
            copy //= 10
            if is_prime(copy):
                right_truncatables.append(prime)
            else:
                break
    right_truncatables = list(set(right_truncatables))
    right_truncatables.sort(reverse=True)
    return right_truncatables