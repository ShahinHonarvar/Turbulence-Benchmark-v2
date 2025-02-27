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
        if is_prime(num):
            primes.add(num)
            while num > 9:
                num //= 10
                if is_prime(num):
                    primes.add(num)
                else:
                    break
        return primes
    right_truncatable_primes = set()
    for num in numbers:
        right_truncatable_primes.update(generate_right_truncatable_primes(num))
    x = numbers[55]
    right_truncatable_primes_less_than_x = [prime for prime in right_truncatable_primes if prime < x]
    return sorted(right_truncatable_primes_less_than_x, reverse=True)