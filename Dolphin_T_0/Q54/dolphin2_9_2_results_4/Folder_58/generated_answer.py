def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[975]
    right_truncatable_primes = []

    def check_right_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[-i:])):
                return False
        return True
    for i in range(2, x):
        if is_prime(i) and check_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)