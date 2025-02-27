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

def left_right_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] == '0':
            return False
        if not is_prime(int(str_n[:i] + str_n[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_val = numbers[6]
    truncatable_primes = []
    for num in range(2, max_val + 1):
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)