def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncate(num: int) -> list[int]:
        return [int(num / 10 ** i) for i in range(len(str(num)))]
    primes = []
    for num in range(2, limit[0] + 1):
        if is_prime(num) and all((is_prime(i) for i in left_truncate(num))):
            primes.append(num)
    return primes