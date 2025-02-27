def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[767]
    primes = [n for n in range(2, x) if is_prime(n)]
    return sorted([n for n in primes if all((is_prime(int(str(n)[-i - 1:])) for i in range(len(str(n)) - 1)))], reverse=True)