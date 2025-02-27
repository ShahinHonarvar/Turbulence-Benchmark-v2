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
        for i in range(1, 10):
            num = i
            while num < n and is_prime(num):
                primes.append(num)
                num = num * 10 + i
        return primes
    x = numbers[6]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes