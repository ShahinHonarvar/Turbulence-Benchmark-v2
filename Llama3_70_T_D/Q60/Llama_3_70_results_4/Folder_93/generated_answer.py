def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        num_str = str(n)
        for _ in range(len(num_str)):
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:-1]
        return True
    x = numbers[11]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if '0' not in str(i) and truncatable(i) and is_prime(i)]
    return sorted(left_right_truncatable_primes)