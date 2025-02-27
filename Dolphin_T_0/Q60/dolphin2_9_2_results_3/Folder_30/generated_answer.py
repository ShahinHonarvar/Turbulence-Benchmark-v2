def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[37]
    primes = []
    for num in range(x, 1, -1):
        if all((is_prime(int(str(num)[i:j + 1])) for i in range(len(str(num))) for j in range(i + 1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)