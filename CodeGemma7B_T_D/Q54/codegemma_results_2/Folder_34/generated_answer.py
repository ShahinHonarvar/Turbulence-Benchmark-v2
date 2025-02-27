def all_right_truncatable_prime(numbers):
    if not isinstance(numbers, tuple):
        raise TypeError('argument must be a tuple')
    if len(numbers) != 19:
        raise ValueError('tuple must have length 19')
    if not all((isinstance(n, int) for n in numbers)):
        raise TypeError('all elements must be integers')
    if not all((n > 0 for n in numbers)):
        raise ValueError('all elements must be positive')
    x = numbers[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)