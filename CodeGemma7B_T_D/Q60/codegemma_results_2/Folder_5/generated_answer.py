def all_left_right_truncatable_prime(t):
    t = t[55]
    for n in range(t + 1):
        if n and all([int(num) < 5 for num in str(n)]) and is_prime(n):
            if is_r_truncatable(n) and is_l_truncatable(n):
                result.append(n)
    return sorted(result) if result else []

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_r_truncatable(n):
    while n > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def is_l_truncatable(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        if n % 10 == 0:
            return False
        n = int(str(n)[1:])
    return True