def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if n < 10 and str(n).isdigit() and is_prime(n):
        return True
    if str(n).isdigit() and is_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i:])):
                return False
        return True
    return False

def all_left_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    result = []
    for num in numbers:
        if num > 0 and is_left_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result