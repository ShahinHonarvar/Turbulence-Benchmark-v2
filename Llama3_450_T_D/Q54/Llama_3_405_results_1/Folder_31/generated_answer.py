def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return True
    x = numbers[50]
    return sorted([i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)], reverse=True)