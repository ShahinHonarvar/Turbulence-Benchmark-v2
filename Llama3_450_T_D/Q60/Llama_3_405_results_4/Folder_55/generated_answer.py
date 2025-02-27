def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            left_trunc = n_str[i:]
            right_trunc = n_str[:-i - 1]
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                return False
        return True
    x = numbers[73]
    truncatable_primes = []
    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)