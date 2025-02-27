def all_left_right_truncatable_prime(numbers):
    x = numbers[35]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not is_prime(int(s)) and (not is_prime(int(s[1:]))):
                return False
            s = s[1:-1]
        return is_prime(n)
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)