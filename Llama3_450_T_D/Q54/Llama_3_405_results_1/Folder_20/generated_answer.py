def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        is_right_truncatable = True
        for i in range(len(num_str)):
            trunc_num = int(num_str[:-i or None])
            if not is_prime(trunc_num):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)