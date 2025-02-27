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
    if n < 10 and is_prime(n):
        return True
    if str(n)[0] == '0' or str(n)[-1] == '0':
        return False
    return is_prime(n) and left_right_truncatable_prime(int(str(n)[1:])) and left_right_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []
    for num in range(2, x + 1):
        if left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)