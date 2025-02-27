def all_left_right_truncatable_prime(numbers):
    x = numbers[26]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            left = int(n_str[i:])
            right = int(n_str[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes)