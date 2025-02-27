import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(r):
    prime_numbers = [i for i in range(2, r + 1) if is_prime(i)]
    prime_numbers = [i for i in prime_numbers if str(i)[0] != '0']
    prime_numbers = [i for i in prime_numbers if is_left_truncatable_prime(i)]
    prime_numbers = [i for i in prime_numbers if is_right_truncatable_prime(i)]
    prime_numbers.sort(reverse=True)
    return prime_numbers