def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        return str(n).count('0') == 0 and all([is_prime(int(str(n)[i:j])) for i, j in zip([0, 1], [len(str(n)) - 2, len(str(n)) - 1])])
    x = numbers[87]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    return sorted([n for n in primes if is_truncatable_prime(n)])