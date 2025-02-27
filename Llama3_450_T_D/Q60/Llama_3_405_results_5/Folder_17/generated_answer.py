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

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = set()
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(1, len(num_str)):
            trunc_left = int(num_str[i:])
            trunc_right = int(num_str[:-i])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)