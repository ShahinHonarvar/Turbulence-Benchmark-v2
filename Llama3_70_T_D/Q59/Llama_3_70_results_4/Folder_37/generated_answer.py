def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    left_truncatables = [i for i in range(2, x) if set(str(i)) != {'0'} and left_truncatable(i) and is_prime(i)]
    return sorted(left_truncatables, reverse=True)