def all_left_truncatable_prime(input_tuple):
    x = input_tuple[38]

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncate(n):
        return int(str(n)[1:])
    ltp_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num = left_truncate(truncated_num)
            if truncated_num == 0:
                ltp_primes.append(num)
    return sorted(ltp_primes, reverse=True)