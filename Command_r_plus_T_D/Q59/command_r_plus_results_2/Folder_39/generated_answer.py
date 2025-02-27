def all_left_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for i in range(2, limit):
            if is_prime(i):
                left_truncatable = True
                temp = i
                while temp > 9:
                    temp //= 10
                    if not is_prime(temp):
                        left_truncatable = False
                        break
                if left_truncatable:
                    primes.append(i)
        return primes
    limit = numbers[30]
    primes = generate_left_truncatable_primes(limit)
    return sorted(primes, reverse=True)