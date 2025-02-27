def all_left_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = input_tuple[49]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num) or not is_prime(num):
            continue
        truncation = num
        while truncation > 1:
            truncation //= 10
            if not is_prime(truncation):
                break
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)