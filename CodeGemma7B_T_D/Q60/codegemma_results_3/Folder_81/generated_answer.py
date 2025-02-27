def all_left_right_truncatable_prime(x: int) -> list[int]:
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)

def is_truncatable_prime(n: int) -> bool:
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)

def is_left_truncatable_prime(n: int) -> bool:
    str_n = str(n)
    for i in range(1, len(str_n)):
        if str_n[i] == '0' or int(str_n[i:]) % 2 == 0:
            return False
        for j in range(3, int(str_n[i:]) ** 0.5 + 1, 2):
            if int(str_n[i:]) % j == 0:
                return False
    return True

def is_right_truncatable_prime(n: int) -> bool:
    str_n = str(n)
    for i in reversed(range(1, len(str_n))):
        if str_n[i] == '0' or int(str_n[:i + 1]) % 2 == 0:
            return False
        for j in range(3, int(str_n[:i + 1] ** 0.5) + 1, 2):
            if int(str_n[:i + 1]) % j == 0:
                return False
    return True