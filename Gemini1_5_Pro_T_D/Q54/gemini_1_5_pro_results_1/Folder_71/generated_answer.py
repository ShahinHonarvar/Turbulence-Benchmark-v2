def all_right_truncatable_prime(numbers):
    x = numbers[22]

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        for i in range(len(str(n))):
            if int(str(n)[:i + 1]) <= 1:
                return False
            if not all([int(str(n)[:i + 1]) % j for j in range(2, int(int(str(n)[:i + 1]) ** 0.5) + 1)]).count(True):
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes