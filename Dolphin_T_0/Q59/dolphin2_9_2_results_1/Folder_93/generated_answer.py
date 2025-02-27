def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[11]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            for length in range(len(num_str) - 1, 0, -1):
                truncated_num = int(num_str[length:])
                if not is_prime(truncated_num) or '0' in str(truncated_num):
                    break
                if length == 1:
                    left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes