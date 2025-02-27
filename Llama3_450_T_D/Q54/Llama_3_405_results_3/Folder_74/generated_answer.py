def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            truncated = str_num[:-1]
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[:-1]
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)