def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_left_truncatable = True
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)