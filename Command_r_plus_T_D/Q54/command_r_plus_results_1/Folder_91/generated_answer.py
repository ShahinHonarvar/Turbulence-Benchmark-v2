def all_right_truncatable_prime(input_tuple: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncate(num: int) -> list[int]:
        truncated_nums = []
        while num > 0:
            truncated_nums.append(num)
            num //= 10
        return truncated_nums
    primes = []
    x = input_tuple[0]
    for num in range(2, x):
        if is_prime(num):
            truncated_nums = right_truncate(num)
            if all((is_prime(n) for n in truncated_nums)):
                primes.append(num)
    return sorted(primes, reverse=True)