def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(integer_tuple):
    x = integer_tuple[618]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and len(str(i)) > 1 and all((is_prime(int(str(i)[j:i.index(str(i)[j], j + 1)])) for j in range(len(str(i)) - 1)))])