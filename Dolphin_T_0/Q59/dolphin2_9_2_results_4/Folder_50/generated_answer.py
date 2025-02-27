def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(given_tuple):
    x = given_tuple[57]
    return sorted([i for i in range(x, 1, -1) if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))])