def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)