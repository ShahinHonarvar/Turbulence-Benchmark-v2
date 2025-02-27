def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x + 1):
        if all((int(num[i:]) in primes or is_prime(int(num[i:])) for i in range(len(num)))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True