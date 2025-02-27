from sortedcontainers import SortedList

def is_prime(n: int) -> bool:
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

def is_truncatable_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
    return True

def all_right_truncatable_prime(tup: tuple[int, ...]) -> list[int]:
    x = tup[98]
    result = SortedList()
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.add(i)
    return list(result)