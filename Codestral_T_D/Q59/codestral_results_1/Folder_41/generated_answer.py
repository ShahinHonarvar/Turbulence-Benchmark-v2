def all_left_truncatable_prime(numbers):
    x = numbers[46]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] or is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

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