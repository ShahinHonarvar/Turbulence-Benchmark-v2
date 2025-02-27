def all_right_truncatable_prime(numbers):
    x = numbers[466]
    right_truncatable_primes = []
    for num in range(2, x):
        is_truncatable_prime = True
        truncated_num = num
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            truncated_num = truncated_num // 10
        if is_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True