def all_right_truncatable_prime(numbers):
    x = numbers[645]
    trunc_primes = []
    for i in range(2, x):
        if all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
            trunc_primes.append(i)
    return sorted(trunc_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True