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
                truncated_num = str(i)
                while len(truncated_num) > 1:
                    truncated_num = truncated_num[1:]
                    if not is_prime(int(truncated_num)):
                        break
                if len(truncated_num) == 1:
                    primes.append(i)
        return primes
    limit = numbers[50]
    primes = generate_left_truncatable_primes(limit)
    return sorted(primes, reverse=True)