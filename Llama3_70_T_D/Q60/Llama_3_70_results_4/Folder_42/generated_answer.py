def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    for _ in range(len(str(n))):
        if not is_prime(int(str(n)[1:])) or not is_prime(int(str(n)[:-1])):
            return False
        n = int(str(n)[1:-1])
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    truncatable_primes = [i for i in range(x, 0, -1) if is_prime(i) and '0' not in str(i) and is_truncatable(i)]
    return truncatable_primes