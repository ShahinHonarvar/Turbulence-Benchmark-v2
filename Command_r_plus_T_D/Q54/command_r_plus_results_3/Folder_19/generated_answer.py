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
            if is_prime(temp):
                primes.add(temp)
        return primes
    x = numbers[67]
    right_truncatable_primes = []
    for num in range(x):
        if is_prime(num):
            right_truncatable_primes.extend(generate_right_truncatable_primes(num))
    right_truncatable_primes_less_than_x = [prime for prime in right_truncatable_primes if prime < x]
    return sorted(right_truncatable_primes_less_than_x, reverse=True)