def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):

    def is_valid(n):
        n = str(n)
        return is_prime(n) and all((is_prime(n[i + 1:j + 1]) for i in range(len(n) - 1) for j in range(i + 1, len(n))))
    return [i for i in range(x + 1) if is_valid(i)]