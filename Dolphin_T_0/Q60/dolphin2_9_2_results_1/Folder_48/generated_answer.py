def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n and n % p != 0:
        p += 2
    return p * p > n

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and all((is_prime(int(str(num)[1:-1])) for _ in range(len(str(num)) - 2))):
            result.append(num)
    return sorted(result)