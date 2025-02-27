def right_truncated_prime(n):
    while n:
        if not str(n)[-1] in '2357' or n % 2 == 0 or n % 5 == 0 or any((n % d == 0 for d in range(3, int(n ** 0.5) + 1, 2))):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[84]
    return sorted((n for n in range(2, x) if right_truncated_prime(n)), reverse=True)