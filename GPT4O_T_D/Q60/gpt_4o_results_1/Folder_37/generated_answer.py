def all_left_right_truncatable_prime(numbers):
    x = numbers[35]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)