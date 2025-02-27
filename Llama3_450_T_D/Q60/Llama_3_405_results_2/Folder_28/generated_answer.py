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

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            truncatable = True
            for i in range(1, len(num_str)):
                trunc_left = int(num_str[i:])
                trunc_right = int(num_str[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)