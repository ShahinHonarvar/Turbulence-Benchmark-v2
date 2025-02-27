def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            trunc_left = int(num_str[i:])
            trunc_right = int(num_str[:len(num_str) - i])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)