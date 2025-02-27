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
    x = numbers[29]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_right_truncatable = True
        for i in range(len(num_str) - 1, -1, -1):
            if not is_prime(int(num_str[:i + 1])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)