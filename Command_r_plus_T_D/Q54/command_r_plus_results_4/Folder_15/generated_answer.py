def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncate(num: int) -> list[int]:
        trunc_list = []
        while num > 0:
            trunc_list.append(num)
            num //= 10
        return trunc_list
    primes = []
    for num in range(numbers[6] - 1, 0, -1):
        if is_prime(num):
            trunc_list = right_truncate(num)
            if all((is_prime(n) for n in trunc_list)):
                primes.append(num)
    return sorted(primes, reverse=True)