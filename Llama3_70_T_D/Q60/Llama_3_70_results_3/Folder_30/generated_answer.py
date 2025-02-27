def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            left_trunc = int(n_str[i:])
            right_trunc = int(n_str[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)