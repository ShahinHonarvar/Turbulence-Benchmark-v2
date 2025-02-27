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

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[36]
    left_truncatables = []
    for n in range(x, 1, -1):
        if is_prime(n):
            trunc = n
            while trunc > 0 and is_prime(trunc):
                trunc //= 10
                if trunc == 0:
                    left_truncatables.append(n)
    return sorted(left_truncatables, reverse=True)