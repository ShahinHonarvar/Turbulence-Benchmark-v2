def all_right_truncatable_prime(numbers):
    x = numbers[87]
    primes = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True