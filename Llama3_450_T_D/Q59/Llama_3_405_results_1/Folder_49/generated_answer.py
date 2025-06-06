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

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    left_truncatable_primes = set()
    for num in range(10, x):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                break
        else:
            left_truncatable_primes.add(num)
    return sorted(list(left_truncatable_primes))