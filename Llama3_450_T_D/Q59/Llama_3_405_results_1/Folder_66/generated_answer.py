def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    truncatable_primes = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        truncatable = True
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)