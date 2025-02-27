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

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    truncatable_primes = set()
    for num in range(11, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)