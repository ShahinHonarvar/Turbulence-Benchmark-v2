def all_left_right_truncatable_prime(numbers):
    x = numbers[91]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        if any((d == '0' for d in str(n))):
            return False
        left = str(n)[1:]
        right = str(n)[:-1]
        while left and right:
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
            left = left[1:]
            right = right[:-1]
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes