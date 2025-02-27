def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[20]
    right_truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        is_right_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes), reverse=True)