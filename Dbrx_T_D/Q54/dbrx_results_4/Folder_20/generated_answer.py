def all_right_truncatable_prime(t: tuple[int]) -> list[int]:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n: int) -> bool:
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    x = t[100]
    result = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)