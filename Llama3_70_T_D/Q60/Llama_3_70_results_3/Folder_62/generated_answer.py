def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    x = numbers[70]
    return sorted([i for i in range(2, x + 1) if '0' not in str(i) and is_prime(i) and is_left_right_truncatable(i)])