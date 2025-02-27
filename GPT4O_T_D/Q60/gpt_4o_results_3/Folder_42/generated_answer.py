def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        if not is_prime(num):
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
                return False
        return True
    x = numbers[64]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)