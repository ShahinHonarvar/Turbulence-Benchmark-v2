def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        left_truncate = int(str_n[i:])
        right_truncate = int(str_n[:len(str_n) - i])
        if not (is_prime(left_truncate) and is_prime(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes