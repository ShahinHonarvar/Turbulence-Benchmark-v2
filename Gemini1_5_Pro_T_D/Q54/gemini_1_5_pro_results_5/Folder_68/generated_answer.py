def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[:-i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    result = []
    for i in range(2, numbers[1]):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result