def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num: int) -> bool:
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    right_truncatable_primes = []
    for num in numbers:
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    x = numbers[89]
    return [num for num in right_truncatable_primes if num < x]