def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers_tuple[618]
    truncable_primes = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        truncated_left = int(str(num)[1:])
        truncated_right = int(str(num)[:-1])
        if is_prime(num) and is_prime(truncated_left) and is_prime(truncated_right):
            truncable_primes.append(num)
    return sorted(truncable_primes)