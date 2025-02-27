def all_right_truncatable_prime(numbers):
    x = numbers[46]
    r = []
    for i in range(2, int(x / 2 + 1.5)):
        if is_prime(i) and x % i == 0:
            r.append(i)
    return sorted(r, reverse=True)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True