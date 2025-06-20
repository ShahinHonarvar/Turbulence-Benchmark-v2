def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:len(num_str) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = numbers[88]
    truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return truncatable_primes