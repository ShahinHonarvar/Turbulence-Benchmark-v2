def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(num: int) -> list[int]:
        primes = []
        for i in range(10 ** len(str(num)) - 1, 1, -1):
            if str(i)[:len(str(num))] == str(num) and is_prime(i):
                primes.append(i)
        return primes
    left_truncatable_primes = []
    for num in range(2, limit[91]):
        if is_prime(num):
            left_truncatable_primes.extend(generate_left_truncatable_primes(num))
    return sorted(set(left_truncatable_primes))