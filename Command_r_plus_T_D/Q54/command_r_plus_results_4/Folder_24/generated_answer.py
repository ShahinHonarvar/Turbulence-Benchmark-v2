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
        if num >= 2 and is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    x = numbers[65]
    right_truncatable_primes = [num for num in right_truncatable_primes if num < x]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes