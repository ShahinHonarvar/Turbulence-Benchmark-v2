def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[52]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_left_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)