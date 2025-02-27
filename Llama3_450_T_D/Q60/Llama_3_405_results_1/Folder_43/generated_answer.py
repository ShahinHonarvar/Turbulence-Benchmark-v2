def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' not in num_str and is_prime(num):
            left_right_truncatable = True
            for i in range(1, len(num_str)):
                left_trunc = int(num_str[i:])
                right_trunc = int(num_str[:-i])
                if not (is_prime(left_trunc) and is_prime(right_trunc)):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)