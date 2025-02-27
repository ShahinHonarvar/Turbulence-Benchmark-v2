def all_left_right_truncatable_prime(numbers):
    x = numbers[18]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10 or '0' in str(n) or (not is_prime(n)):
            return False
        left, right = (str(n)[1:], str(n)[:-1])
        while left and right:
            if not (is_prime(int(left)) and is_prime(int(right))):
                return False
            left, right = (left[1:], right[:-1])
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes