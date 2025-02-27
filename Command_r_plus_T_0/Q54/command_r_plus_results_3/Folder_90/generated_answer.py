def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(num: int) -> list[int]:
        primes = []
        while num > 0:
            if is_prime(num):
                primes.append(num)
            num //= 10
        return primes
    right_truncatable_primes = []
    for num in numbers:
        if num > 0:
            primes = generate_right_truncatable_primes(num)
            right_truncatable_primes.extend(primes)
    right_truncatable_primes = list(set(right_truncatable_primes))
    right_truncatable_primes.sort(reverse=True)
    x = numbers[466]
    right_truncatable_primes = [prime for prime in right_truncatable_primes if prime < x]
    return right_truncatable_primes