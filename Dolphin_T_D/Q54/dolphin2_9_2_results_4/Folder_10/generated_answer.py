def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[38]
    right_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        truncation = number
        while truncation:
            if not is_prime(truncation):
                break
            truncation //= 10
        else:
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)