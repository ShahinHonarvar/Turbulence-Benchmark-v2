def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            left = n[i:]
            right = n[:len(n) - i]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            primes.add(i)
    return sorted(list(primes), reverse=True)