def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_right_truncatable_prime = True
        for i in range(len(num_str)):
            truncated_num_str = num_str[:-i or None]
            truncated_num = int(truncated_num_str)
            if not is_prime(truncated_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)