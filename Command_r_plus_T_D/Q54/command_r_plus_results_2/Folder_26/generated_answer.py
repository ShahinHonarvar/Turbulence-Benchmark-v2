def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(n: int) -> set[int]:
        primes = set()
        for i in range(10 ** n, 10 ** (n + 1)):
            if all((is_prime(i // 10 ** j * 10 ** (n - j)) for j in range(n))):
                primes.add(i)
        return primes
    limit = numbers[81]
    primes = generate_right_truncatable_primes(len(str(limit)))
    return sorted(list(primes), reverse=True)