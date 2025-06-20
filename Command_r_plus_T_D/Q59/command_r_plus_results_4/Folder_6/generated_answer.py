def all_left_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num: int) -> bool:
        if str(num).count('0') > 0:
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return True
    left_truncatable_primes = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    x = numbers[74]
    left_truncatable_primes = [prime for prime in left_truncatable_primes if prime < x]
    left_truncatable_primes.sort()
    return left_truncatable_primes