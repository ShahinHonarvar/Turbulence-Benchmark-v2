def all_left_right_truncatable_prime(numbers):
    x = numbers[81]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def has_no_zero(n):
        return '0' not in str(n)

    def is_left_right_truncatable_prime(number):
        num_str = str(number)
        while len(num_str) > 1:
            num_str = num_str[1:-1]
            if not is_prime(int(num_str)):
                return False
        return True
    primes = [n for n in range(2, x + 1) if is_prime(n) and has_no_zero(n)]
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)