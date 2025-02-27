def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[49]
    primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        if not is_prime(n):
            continue
        truncate_left_right = str(n)
        while truncate_left_right and truncate_right_left:
            if '0' in truncate_left_right or not is_prime(int(truncate_left_right)):
                break
            if '0' in truncate_right_left or not is_prime(int(truncate_right_left)):
                break
            truncate_left_right = truncate_left_right[1:]
            truncate_right_left = truncate_right_left[:-1]
        if not truncate_left_right and (not truncate_right_left):
            primes.append(n)
    return sorted(primes)