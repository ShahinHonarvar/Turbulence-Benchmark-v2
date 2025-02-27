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
        return primes[::-1]
    right_truncatable_primes = []
    for num in numbers:
        right_truncatable_primes.extend(generate_right_truncatable_primes(num))
    x = numbers[92]
    right_truncatable_primes = [prime for prime in right_truncatable_primes if prime < x]
    right_truncatable_primes.sort()
    return right_truncatable_primes