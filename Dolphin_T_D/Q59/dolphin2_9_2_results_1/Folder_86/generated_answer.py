def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for i in range(x - 1, 0, -1):
        if not is_prime(i) or '0' in str(i):
            continue
        temp = i
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            primes.append(i)
    return primes