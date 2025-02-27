def all_left_right_truncatable_prime(x):
    output = []
    for n in range(2, x + 1):
        if left_right_truncatable_prime(n):
            output.append(n)
    return sorted(output)

def left_right_truncatable_prime(n):
    if not contains_zero(n):
        if n in [2, 3, 5, 7]:
            return True
        if n % 2 != 0 and n % 5 != 0 and all([n % d != 0 for d in range(3, int(n ** 0.5) + 1, 2)]):
            return True
    return False

def contains_zero(n):
    return '0' in str(n)