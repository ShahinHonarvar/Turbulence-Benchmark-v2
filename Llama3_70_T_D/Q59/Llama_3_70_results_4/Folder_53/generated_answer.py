def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            if all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
                if is_prime(i):
                    left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)