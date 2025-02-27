def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(n: int) -> list[int]:
        primes = []
        for i in range(10 ** n):
            num = i
            for _ in range(n):
                if not is_prime(num):
                    break
                num //= 10
            else:
                primes.append(i)
        return primes
    x = numbers[6]
    primes = generate_right_truncatable_primes(len(str(x)))
    right_truncatable_primes = [prime for prime in primes if prime < x]
    return sorted(right_truncatable_primes, reverse=True)