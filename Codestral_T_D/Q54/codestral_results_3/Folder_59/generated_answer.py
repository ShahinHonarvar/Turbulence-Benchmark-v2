def all_right_truncatable_prime(numbers):
    x = numbers[84]
    result = []
    for num in range(x - 1, 1, -1):
        if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True