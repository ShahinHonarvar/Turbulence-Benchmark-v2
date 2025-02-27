def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncate(n):
        n_str = str(n)
        for _ in range(len(n_str) - 2):
            n_str = n_str[1:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    x = numbers[98]
    primes = [i for i in range(2, x + 1) if is_prime(i) and is_truncate(i)]
    return primes