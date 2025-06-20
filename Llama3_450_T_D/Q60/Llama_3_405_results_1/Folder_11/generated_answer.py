def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str)):
            trunc_left = num_str[i:]
            trunc_right = num_str[:-i or len(num_str)]
            if not (is_prime(int(trunc_left)) and is_prime(int(trunc_right))):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)