def all_left_truncatable_prime(n):
    first_digit = n // 10 ** (len(str(n)) - 1)
    if first_digit == 0:
        return []
    if not is_prime(n):
        return []
    if is_prime(n % 10 ** (len(str(n)) - 1)):
        return [n]
    return all_left_truncatable_prime(n % 10 ** (len(str(n)) - 1))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True