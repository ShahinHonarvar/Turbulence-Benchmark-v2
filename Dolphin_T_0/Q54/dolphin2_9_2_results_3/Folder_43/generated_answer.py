def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(args):
    x = args[89]
    numbers = []
    for n in range(x - 1, 0, -1):
        if is_right_truncatable_prime(n):
            numbers.append(n)
    return sorted(numbers, reverse=True)