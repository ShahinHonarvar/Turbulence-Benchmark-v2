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

def remove_left_digit(n):
    while n > 9:
        n //= 10
    return n

def remove_right_digit(n):
    return n // 10 if n > 9 else 1

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[93]
    l_r_truncatable_primes = []
    for num in range(10, x + 1):
        if not str(num).startswith('0') and is_prime(num):
            is_l_r_truncatable = True
            for _ in range(len(str(num)) - 1):
                if not is_prime(remove_left_digit(num)) or not is_prime(remove_right_digit(num)):
                    is_l_r_truncatable = False
                    break
            if is_l_r_truncatable:
                l_r_truncatable_primes.append(num)
    return sorted(l_r_truncatable_primes)