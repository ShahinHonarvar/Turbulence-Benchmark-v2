def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(p):
        if p <= 1:
            return False
        for i in range(len(str(p)) - 1, 0, -1):
            if not is_prime(int(str(p)[i:])):
                return False
        return True
    x = numbers[26]
    primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(primes)