def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = str(num)
            while len(truncated_num) > 1:
                truncated_num = truncated_num[:-1]
                if not is_prime(int(truncated_num)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)