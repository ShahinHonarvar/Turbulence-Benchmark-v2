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
        for num in range(limit):
            if is_prime(num):
                digits = list(str(num))
                for i in range(len(digits)):
                    truncated_num = int(''.join(digits[:i]))
                    if not is_prime(truncated_num):
                        break
                else:
                    primes.append(num)
        return primes
    limit = numbers[87]
    right_truncatable_primes = generate_right_truncatable_primes(limit)
    return sorted(right_truncatable_primes)