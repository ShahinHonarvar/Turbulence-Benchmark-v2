def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if is_prime(n):
            current = n
            while current > 0:
                if not is_prime(current):
                    return False
                current //= 10
            return True
        return False
    x = numbers[77]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)