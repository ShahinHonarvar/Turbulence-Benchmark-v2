def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) > 1 and int(str(num)[:i]) not in primes and (int(str(num)[i:]) > 1) and (int(str(num)[i:]) not in primes) for i in range(1, len(str(num))))) and is_prime(num):
            primes.append(num)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True