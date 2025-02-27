def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for i in range(1, 10):
            current_num = i
            while current_num < limit:
                if is_prime(current_num):
                    primes.append(current_num)
                current_num = current_num * 10 + i
        return primes
    limit = numbers[39]
    right_truncatable_primes = generate_right_truncatable_primes(limit)
    right_truncatable_primes.sort()
    return right_truncatable_primes