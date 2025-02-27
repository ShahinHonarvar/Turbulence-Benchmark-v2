def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[70]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        num_str = str(num)
        truncatable = True
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)