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
            truncated_prime = True
            for _ in range(n):
                if not is_prime(num):
                    truncated_prime = False
                    break
                num //= 10
            if truncated_prime and is_prime(i):
                primes.append(i)
        return primes
    x = numbers[97]
    right_truncatable_primes = generate_right_truncatable_primes(len(str(x)))
    return sorted([i for i in right_truncatable_primes if i < x])