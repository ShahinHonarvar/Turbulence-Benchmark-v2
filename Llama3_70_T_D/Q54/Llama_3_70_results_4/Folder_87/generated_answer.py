def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_right_truncatable(n):
    str_num = str(n)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(right_truncatable_primes, reverse=True)