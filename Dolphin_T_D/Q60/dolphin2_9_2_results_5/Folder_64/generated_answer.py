def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        if set(n) != {'1', '3', '7', '9'} or n[0] + n[-1] in ['0', '2', '4', '6', '8']:
            return False
        return all((int(n[i:j]) != 0 and is_prime(int(n[i:j])) for i in range(len(n)) for j in range(i + 1, len(n) + 1)))
    return sorted((n for n in range(2, x + 1) if is_prime(n) and is_truncatable_prime(n)))