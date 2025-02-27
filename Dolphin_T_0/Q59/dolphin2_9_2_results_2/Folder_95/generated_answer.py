def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def all_left_truncatable_prime(numbers):
    primes = []
    x = numbers[77]
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            if all((is_prime(int(str(i)[n:])) for n in range(1, len(str(i))))):
                primes.append(i)
    return sorted(primes)