def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    x = numbers[55]
    left_truncatable_primes = [i for i in range(x - 1, 1, -1) if is_left_truncatable_prime(i) and is_prime(i)]
    return left_truncatable_primes