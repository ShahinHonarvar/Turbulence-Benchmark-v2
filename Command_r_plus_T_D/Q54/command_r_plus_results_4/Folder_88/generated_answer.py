def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> set[int]:
        primes = set()
        for i in range(10 ** len(str(num)) - 1, 0, -1):
            temp = num + i
            if is_prime(temp) and all((is_prime(int(str(temp)[:j])) for j in range(len(str(temp))))):
                primes.add(temp)
        return primes
    x = numbers[93]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(list(right_truncatable_primes))