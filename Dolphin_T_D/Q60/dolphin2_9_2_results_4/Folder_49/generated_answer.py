def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_truncatable(prime):
    if '0' in str(prime):
        return False
    while len(str(prime)) > 1:
        if not is_prime(int(str(prime)[1:-1])):
            return False
        prime = int(str(prime)[1:-1])
    return True

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(2, x + 1) if is_truncatable(i) and is_prime(i)])