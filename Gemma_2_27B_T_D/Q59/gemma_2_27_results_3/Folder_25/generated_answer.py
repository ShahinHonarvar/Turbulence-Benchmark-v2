def all_left_truncatable_prime(numbers):
    x = numbers[92]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] or is_prime(int(str(i)[:j])) for j in range(1, len(str(i)) + 1))) and all((int(str(i)[:j]) != 0 for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True