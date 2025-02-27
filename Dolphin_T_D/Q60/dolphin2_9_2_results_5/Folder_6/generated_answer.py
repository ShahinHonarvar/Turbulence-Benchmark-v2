def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 1:
        if '0' in str(n) or not all((str(n)[:k] + str(n)[k + 1:] in [2, 3, 5, 7] for k in range(len(str(n)) - 1))):
            return False
        n /= 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i) and all((primes[j] < i or primes[j] % i != 0 for j in range(len(primes)))):
            primes.append(i)
    return primes