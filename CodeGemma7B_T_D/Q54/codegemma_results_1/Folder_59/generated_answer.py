def all_right_truncatable_prime(t: tuple[int]) -> list[int]:
    ans = []
    for x in range(t[84], 0, -1):
        if is_tm_prime(x):
            digit = get_digit(x, 0)
            if is_prime(x):
                ans.append(x)
    return sorted(ans, reverse=True)

def is_tm_prime(n: int) -> bool:
    return is_prime(n) and (not is_prime(int(str(n)[:-1])))

def get_digit(n: int, k: int) -> int:
    arr = reversed(str(n))
    if len(arr) <= k:
        return 0
    return int(next(arr) if k else '0')

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True