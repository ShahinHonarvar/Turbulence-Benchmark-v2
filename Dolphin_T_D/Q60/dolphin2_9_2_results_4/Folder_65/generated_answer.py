def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    if x <= 2:
        return []
    x = list(map(int, str(x)))
    left_right_truncatable_prime = []

    def is_left_right_truncatable(n):
        while n > 9:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    for num in range(2, int(x) + 1):
        if is_left_right_truncatable(num):
            left_right_truncatable_prime.append(num)
    return left_right_truncatable_prime