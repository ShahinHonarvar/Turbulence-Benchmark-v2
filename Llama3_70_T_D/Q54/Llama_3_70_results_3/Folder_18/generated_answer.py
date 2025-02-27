def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return True
    x = numbers[429]
    truncatable_primes = [i for i in range(2, x) if right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)