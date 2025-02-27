def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return True
    x = numbers[29]
    primes = [i for i in range(2, x + 1) if is_prime(i) and left_right_truncatable(i)]
    return sorted(primes, reverse=True)