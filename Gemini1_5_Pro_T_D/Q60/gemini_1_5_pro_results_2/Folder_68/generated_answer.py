def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[1]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            is_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                left_truncated = int(num_str[i:])
                right_truncated = int(num_str[:-i])
                if not (is_prime(left_truncated) and is_prime(right_truncated)):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)