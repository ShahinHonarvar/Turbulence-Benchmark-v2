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

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(p):
        if not is_prime(p):
            return False
        str_p = str(p)
        while len(str_p) > 1:
            str_p = str_p[:-1]
            if not is_prime(int(str_p)):
                return False
        return True
    x = numbers[65]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)