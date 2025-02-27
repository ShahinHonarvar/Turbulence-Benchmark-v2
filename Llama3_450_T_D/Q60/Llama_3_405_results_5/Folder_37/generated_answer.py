def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            trunc_left = int(num_str[i:])
            trunc_right = int(num_str[:len(num_str) - i])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                return False
        return True
    x = numbers[35]
    truncatable_primes = [i for i in range(2, x + 1) if '0' not in str(i) and is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)