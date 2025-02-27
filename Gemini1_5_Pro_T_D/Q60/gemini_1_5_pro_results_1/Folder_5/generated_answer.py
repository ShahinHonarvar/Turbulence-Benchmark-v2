def all_left_right_truncatable_prime(numbers):
    x = numbers[55]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        left = str(n)
        right = str(n)
        while len(left) > 1:
            left = left[1:]
            right = right[:-1]
            if not (is_prime(int(left)) and is_prime(int(right))):
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes