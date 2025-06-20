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
                digits = list(str(i))
                left_truncatable = True
                for _ in range(len(digits)):
                    digits.pop(0)
                    if not is_prime(int(''.join(digits))):
                        left_truncatable = False
                        break
                if left_truncatable:
                    primes.append(i)
        return primes
    limit = numbers[433]
    left_truncatable_primes = generate_left_truncatable_primes(limit)
    sorted_primes = sorted(left_truncatable_primes, reverse=True)
    return sorted_primes