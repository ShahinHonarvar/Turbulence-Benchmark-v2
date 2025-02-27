def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                j //= 10
                if not is_prime(j):
                    break
            else:
                primes.append(i)
    return sorted(primes)