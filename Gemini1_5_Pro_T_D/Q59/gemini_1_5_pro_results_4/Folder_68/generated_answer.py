def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    return is_left_truncatable_prime(int(str(n)[1:]))

def all_left_truncatable_prime(numbers):
    result = []
    for i in range(2, numbers[1]):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result